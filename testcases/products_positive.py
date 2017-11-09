from tools.dbconnect import DBCONNECT
from tools.req import REQ
import json

req = REQ()
db_connect = DBCONNECT()

def create_product():
    """

    :return:
    """

    global product_id
    global rs_price
    global rs_title
    name = "Tests1"
    price = "9.99"
    input_data = {

            "name": name,
            "type": "simple",
            "regular_price": price}
    #         "description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.",
    #         "short_description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
    #         "categories": [
    #             {
    #                 "id": 9
    #             },
    #             {
    #                 "id": 14
    #             }
    #         ],
    #         "images": [
    #             {
    #                 "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_front.jpg",
    #                 "position": 0
    #             },
    #             {
    #                 "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_back.jpg",
    #                 "position": 1
    #             }
    #         ]
    #     }
    # }

    info = req.test_post(endpoint='products',data=input_data)
    print(info[0])
    print(json.dumps(info[1],indent = 4))


    product_id = info[1]['id']
    rs_title = info[1]['name']
    rs_price = info[1]['price']
    # print(product_id)



def test_product_created():
    """

    :return:

    """

    sql = """select p.post_title,pm.meta_value,p.post_type from `wptf_posts` as p Join `wptf_postmeta` as pm 
    on pm.`post_id` = p.`ID` where pm.`meta_key`='_regular_price' and p.`ID`={}""".format(product_id)

    qrs = db_connect.select(db="wp163",query=sql)

    assert qrs[0][0] == rs_title , "The db title is not as expected. DB title {}, Expected {}".format(qrs[0][0],rs_title)
    assert qrs[0][1] == rs_price , "The db price is not as expected. DB price {}, Expected {}".format(qrs[0][1],rs_price)
    assert qrs[0][2] == "product" , "The db product is not as expected. DB price {}, Expected {}".format(qrs[0][2],"product")



create_product()
test_product_created()