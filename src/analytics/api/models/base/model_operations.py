from pymongo import ASCENDING, DESCENDING


class ModelOperations:

    def aggregate(self, stages):
        """
        Am method where documents enter a multi-stage pipeline (defined by the order of the stages) that transforms
        the documents into aggregated results. https://docs.mongodb.com/manual/core/aggregation-pipeline/ for more details
        Args:
            stages: a list that defines various stages to be performed on the documents inorder to achieve a final
                      aggregated results

        Returns: A cursor to the documents that match the query criteria. When the find() method “returns documents,”
                 the method is actually returning a cursor to the documents.

        """

        return self.collection.aggregate(stages)

    def find(self, *args, **kwargs):
        return self.collection.find(*args, **kwargs)

    def sort(self, key, ascending=True):
        if not key:
            raise Exception("sort key cannot be empty")
        return self.collection.find().sort(key, ASCENDING if ascending else DESCENDING)

    def _init_filter_dict(self):
        self.andOperatorKey = "$and"
        self.filter_dict = {self.andOperatorKey: []}

    def _get_filter_dict(self):
        try:
            return self.filter_dict
        except AttributeError:
            self._init_filter_dict()
            return self.filter_dict

    def _update_filter_dict(self, **new_filters):
        """
        Method  for updating the filter_dict attr of self. Emphasis is placed on splitting the new filters into
        single-key dict that mongo $and operator expects.

        Args:
            **new_filters: a dict containing the new filter conditions
        """

        filter_dict = self._get_filter_dict()
        filters = filter_dict[self.andOperatorKey]
        split_filters = [{key: value} for key, value in new_filters.items()]
        filters.extend(split_filters)

        filter_dict.update({self.andOperatorKey: filters})

        self.filter_dict = filter_dict

    def filter_by(self, *args, **filters):
        """
        A filter method that allows for the chaining style of filtering for example
        model.filter_by(first_name='john', last_name='doe').filter_by(city='kampala').exec().
        The chaining is terminated by the exec() method that clears the filter_dict and queries for results

        Args:
            *args: List of positional arguments
            **filters: a dict of the supplied filter conditions

        Returns: the class instance (self) to enable further chaining
        """
        if args:
            raise Exception("positional arguments are not allowed")

        self._update_filter_dict(**filters)

        return self

    def in_filter_by(self, **filters):
        """
        A filter method that allows for the chaining style of filtering for example
        model.in_filter_by(first_name='john', last_name='doe').in_filter_by(city='kampala').exec().
        The chaining is terminated by the exec() method that clears the filter_dict and queries for results

        This differs from the filter_by method by;
            1. The values of the filters are sequence
            2. This filter maps to the $in mongodb query operator https://docs.mongodb.com/manual/reference/operator/query/in/

        Args:
            **filters:

        Returns:

        """
        modified_filters = {}
        for key, value in filters.items():

            if not isinstance(value, list):
                raise Exception("keys must be instance of list")
            modified_filters[key] = {"$in": value}

        self._update_filter_dict(**modified_filters)

        return self

    def exec(self, projections=None):
        """
        This is a method used to terminate the chained filter query
        Args:
            projections: an optional dict that specifies Specifies the fields to return in the documents that match
                         the query filter. To return all fields in the matching documents, omit this parameter.
                         For details, see https://docs.mongodb.com/manual/reference/method/db.collection.find/#find-projection

        Returns: A cursor to the documents that match the query criteria. When the find() method “returns documents,”
                 the method is actually returning a cursor to the documents.

        """

        filters = self._get_filter_dict()
        self._init_filter_dict()
        projections = projections if projections else {}

        return self.find(filters, projections)

    def convert_model_ids(self, documents):
        docs = list(documents)

        for document in docs:
            for k, v in dict(document).items():
                if k == '_id':
                    document[k] = str(v)
                if v and isinstance(v, list) and isinstance(v[0], dict):
                    self.convert_model_ids(v)
        return docs

