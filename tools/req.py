from woocommerce import API

class REQ():

    def __init__(self):

        admin_consumer_key = "ck_d995de3df62f551d75faf195d785c6ba8de4931e"
        admin_consumer_secret = "cs_19437bf2ca3287f9900dc47d2ec62020d98f2ed0"

        self.wcapi = API(
            url="http://127.0.0.1/wordpressStore/",
            consumer_key=admin_consumer_key,
            consumer_secret=admin_consumer_secret,
            wp_api=True,
            version="wc/v1")

    def test_api(self):
        """

        :return:
        """
        print(self.wcapi.get("").json())

    def test_post(self,endpoint,data):
        """

        :param endpoint:
        :param data:
        :return:
        """
        result = self.wcapi.post(endpoint=endpoint,data=data)
        rs_status = result.status_code
        rs_body = result.json()
        rs_url = result.url

        return [rs_status,rs_body,rs_url ]

    def test_get(self,endpoint):
        """

        :param endpoint:
        :return:

        """
        result = self.wcapi.get(endpoint=endpoint)
        rs_status = result.status_code
        rs_body = result.json()
        rs_url = result.url
        return [rs_status, rs_body, rs_url]

x = REQ()
x.test_api()