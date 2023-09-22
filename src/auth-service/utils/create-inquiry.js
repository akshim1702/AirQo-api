const InquiryModel = require("@models/Inquiry");
const { logObject, logElement, logText } = require("./log");
const mailer = require("./mailer");
const httpStatus = require("http-status");
const constants = require("@config/constants");
const log4js = require("log4js");
const isEmpty = require("is-empty");
const logger = log4js.getLogger(`${constants.ENVIRONMENT} -- inquire-util`);

const inquire = {
  create: async (inquire) => {
    try {
      const {
        fullName,
        email,
        message,
        category,
        tenant,
        firstName,
        lastName,
      } = inquire;

      let name = fullName;

      if (isEmpty(fullName)) {
        name = firstName;
      }

      const responseFromCreateInquiry = await InquiryModel(tenant).register(
        inquire
      );

      if (responseFromCreateInquiry.success === true) {
        const createdInquiry = await responseFromCreateInquiry.data;
        const responseFromSendEmail = await mailer.inquiry(
          name,
          email,
          category,
          message,
          tenant
        );

        if (responseFromSendEmail.success === true) {
          return {
            success: true,
            message: "inquiry successfully created",
            data: createdInquiry,
            status: responseFromSendEmail.status || "",
          };
        } else if (responseFromSendEmail.success === false) {
          logObject("responseFromSendEmail", responseFromSendEmail);
          return responseFromSendEmail;
        }
      } else if (responseFromCreateInquiry.success === false) {
        return responseFromCreateInquiry;
      }
    } catch (e) {
      return {
        success: false,
        message: "Internal Server Error",
        errors: { message: e.message },
        status: httpStatus.INTERNAL_SERVER_ERROR,
      };
    }
  },

  list: async ({ tenant, filter, limit, skip }) => {
    try {
      logElement("the tenant", tenant);
      logObject("the filter", filter);
      logElement("limit", limit);
      logElement("the skip", skip);

      let responseFromListInquiry = await InquiryModel(
        tenant.toLowerCase()
      ).list({
        filter,
        limit,
        skip,
      });

      if (responseFromListInquiry.success == true) {
        return {
          success: true,
          message: responseFromListInquiry.message,
          data: responseFromListInquiry.data,
        };
      } else if (responseFromListInquiry.success == false) {
        if (responseFromListInquiry.error) {
          return {
            success: false,
            message: responseFromListInquiry.message,
            error: responseFromListInquiry.error,
          };
        } else {
          return {
            success: false,
            message: responseFromListInquiry.message,
          };
        }
      }
    } catch (e) {
      return {
        success: false,
        message: "utils server error",
        error: e.message,
      };
    }
  },

  update: async (tenant, filter, update) => {
    try {
      let responseFromModifyInquiry = await InquiryModel(
        tenant.toLowerCase()
      ).modify({
        filter,
        update,
      });
      logObject("responseFromModifyInquiry", responseFromModifyInquiry);
      if (responseFromModifyInquiry.success == true) {
        return {
          success: true,
          message: responseFromModifyInquiry.message,
          data: responseFromModifyInquiry.data,
        };
      } else if (responseFromModifyInquiry.success == false) {
        if (responseFromModifyInquiry.error) {
          return {
            success: false,
            message: responseFromModifyInquiry.message,
            error: responseFromModifyInquiry.error,
          };
        } else {
          return {
            success: false,
            message: responseFromModifyInquiry.message,
          };
        }
      }
    } catch (e) {
      return {
        success: false,
        message: "util server error",
        error: e.message,
      };
    }
  },

  delete: async (tenant, filter) => {
    try {
      let responseFromRemoveInquiry = await InquiryModel(
        tenant.toLowerCase()
      ).remove({
        filter,
      });

      if (responseFromRemoveInquiry.success == true) {
        return {
          success: true,
          message: responseFromRemoveInquiry.message,
          data: responseFromRemoveInquiry.data,
        };
      } else if (responseFromRemoveInquiry.success == false) {
        if (responseFromRemoveInquiry.error) {
          return {
            success: false,
            message: responseFromRemoveInquiry.message,
            error: responseFromRemoveInquiry.error,
          };
        } else {
          return {
            success: false,
            message: responseFromRemoveInquiry.message,
          };
        }
      }
    } catch (e) {
      return {
        success: false,
        message: "util server error",
        error: e.message,
      };
    }
  },
};

module.exports = inquire;
