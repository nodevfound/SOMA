# SOMA

There is something wrong with identification of URL and binary data, commented out the auto-detection code
    
    def __create_header_and_body(self, image_url_or_binary):
        headers = {
            "Ocp-Apim-Subscription-Key": self.__ocp_apim_key
        }
        body = {}

        #if isinstance(image_url_or_binary, str):
        #    headers["Content-type"] = "application/json"
        #    body = json.dumps({"Url": image_url_or_binary})
        #else:
        #    headers["Content-type"] = "application/octet-stream"
        #    body = image_url_or_binary
        headers["Content-type"] = "application/octet-stream"
        body = image_url_or_binary


        return headers, body
