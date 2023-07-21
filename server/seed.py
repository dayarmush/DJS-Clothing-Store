from models.favorites import Favorite
from models.items import Item
from models.reviews import Review
from models.shopping_cart import ShoppingCart
from models.user import User
from config import db
from app import app
from faker import Faker
from random import choice as rc, randint

fake = Faker()

# Add User id
def create_favorites():
    faves = []
    for i in range(30):
        fave = Favorite(
            user_id=randint(1, 30),
            item_id=randint(1, 100)
        )
        faves.append(fave)
    return [fave.id for fave in faves], faves

# add Cart id and Favorite id
def create_items():
    categories =  ["Men's", "Women's", 'kids']
    clothing_items = [
        "T-shirt",
        "Jeans",
        "Dress",
        "Sweater",
        "Hoodie",
        "Shorts",
        "Skirt",
        "Blouse",
        "Blazer",
        "Suit",
        "Coat",
        "Jacket",
        "Vest",
        "Tank top",
        "Cardigan",
        "Jumpsuit",
        "Romper",
        "Polo shirt",
        "Sweatshirt",
        "Leggings",
        "Cargo pants",
        "Capri pants",
        "Overalls",
        "Pajamas",
        "Bathrobe",
        "Onesie",
        "Trench coat",
        "Peacoat",
        "Kimono",
        "Sarong",
        "Maxi dress",
        "Mini skirt",
        "Midi dress",
        "Crop top",
        "Chinos",
        "Flannel shirt",
        "Camisole",
        "Halter top",
        "Poncho",
        "Shawl",
        "Kaftan",
        "Anorak",
        "Windbreaker",
        "Raincoat",
        "Parka",
        "Turtleneck",
        "Polo dress",
        "Sun dress",
        "Tuxedo",
        "Tuxedo dress",
        "Ruffled blouse",
        "Pencil skirt",
        "A-line skirt",
        "Culottes",
        "Cargo shorts",
        "Athletic shorts",
        "Denim jacket",
        "Leather jacket",
        "Suede jacket",
        "Down jacket",
        "Kimono jacket",
        "Off-the-shoulder top",
        "Button-up shirt",
        "Puffer coat",
        "Sheath dress",
        "Jeggings",
        "Harem pants",
        "Capris",
        "Cap sleeve top",
        "Bell-bottoms",
        "Jumper dress",
        "Bandeau top",
        "Fishnet stockings",
        "Pashmina scarf",
        "Ascot tie",
        "Headband",
        "Leg warmers",
        "Newsboy cap",
        "Beret",
        "Bow tie",
        "Necktie",
        "Pocket square",
        "Cravat",
        "Bowler hat",
        "Beanie",
        "Fedora",
        "Visor",
        "Snapback cap",
        "Boater hat",
        "Newsboy cap",
        "Trench dress",
        "Tunic dress",
        "Cold shoulder top",
        "Ringer T-shirt",
        "Joggers",
        "Biker jacket",
        "Chore coat",
        "Peplum top",
        "Tulle skirt",
        "Palazzo pants"
    ]
    items = []
    for i in range(100):
        item = Item(
            name=rc(clothing_items),
            image=fake.file_extension(category='image'),
            price=randint(1, 100),
            category=rc(categories)
        )
        items.append(item)
    return [item.id for item in items], items

# Add Item id and User id 
def create_reviews():
    reviews = []
    for i in range(90):
        review = Review(
            text=fake.sentence(),
            rating=randint(0, 5),
            user_id=randint(1, 30),
            item_id=randint(1, 100)
        )
        reviews.append(review)
    return [review.id for review in reviews], reviews

# Add User id 
def create_carts():
    carts = []
    for i in range(10):
        cart = ShoppingCart(
            user_id=randint(1, 30),
            item_id=randint(1, 100)
        )
        carts.append(cart)
    return [cart.id for cart in carts], carts

def create_users():
    users = []
    for i in range(30):
        user = User(
            username=fake.name(),
        )
        user.password_hash = fake.last_name()
        users.append(user)
    return [user.id for user in users], users

if __name__ == '__main__':
    with app.app_context():
        print('Clearing db...')
        User.query.delete()
        ShoppingCart.query.delete()
        Review.query.delete()
        Item.query.delete()
        Favorite.query.delete()

        print('seeding db...')
        users_id, users = create_users()
        carts_id, carts = create_carts()
        faves_id, favorites = create_favorites()
        items_id, items = create_items()
        reviews_id, reviews = create_reviews()

        # Might need to be in parens
        print('adding to db...')
        db.session.add_all(users)
        db.session.add_all(carts)
        db.session.add_all(favorites)
        db.session.add_all(items)
        db.session.add_all(reviews)
        db.session.commit()

# -------------------------------------------------

# from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Text
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base
# from faker import Faker
# from random import randint

# # Initialize Faker
# fake = Faker()

# # Setting up the engine and session
# engine = create_engine('sqlite:///:memory:', echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()

# Base = declarative_base()

# # Defining the ORM classes
# class Item(Base):
#     __tablename__ = 'items'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     category = Column(String(50))
#     image = Column(String(200))
#     price = Column(Float)
#     reviews = relationship('Review', backref='item', lazy=True)

# class Review(Base):
#     __tablename__ = 'reviews'

#     id = Column(Integer, primary_key=True)
#     item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
#     review_text = Column(Text)
#     rating = Column(Float)

# # Creating the tables
# Base.metadata.create_all(engine)

# # Function to generate clothing items and their reviews
# def create_items_and_reviews(clothing_items):
#     items = []
#     reviews = []

#     for category, category_items in clothing_items.items():
#         for item_name, item_details in category_items.items():
#             # Create an Item object
#             item = Item(name=item_name, category=category, image=item_details['image'], price=item_details['price'])
#             items.append(item)
#             # Add the item to the session so that it gets an ID
#             session.add(item)
#             session.flush()  # This will assign an ID to the item
#             # Create a Review object for this item
#             for _ in range(randint(1, 10)):  # Assign 1-10 reviews per item
#                 review = Review(item_id=item.id, review_text=fake.text(), rating=randint(1, 5))
#                 reviews.append(review)
#     # Add all items and reviews to the session and commit
#     session.add_all(items)
#     session.add_all(reviews)
#     session.commit()
__________________________________________________
#     clothing_items = {
#         "Men's": {
#             "T-shirt": {'image': 'https://imgs.michaels.com/MAM/assets/1/5E3C12034D34434F8A9BAAFDDF0F8E1B/img/617E940D442246D4AA2F229D24F20BAE/10707691_1.jpg', 'price': 20},
#             "Jeans": {'image': 'https://m.media-amazon.com/images/I/81qCSIMK6QL._AC_UF894,1000_QL80_.jpg', 'price': 50},
#             "Dress Shirt": {'image': 'https://www.amedeoexclusive.com/cdn/shop/products/AEBD8054_2_1200x.progressive.jpg?v=1598429697', 'price': 30},
#             "Suit": {'image': 'https://i.pinimg.com/originals/98/3f/55/983f55888eb0ca318d79dd1515ba3498.jpg', 'price': 100},
#             "Blazer": {'image': 'https://m.media-amazon.com/images/I/61AP9GoC+jL.jpg', 'price': 80},
#             "Sweater": {'image': 'https://www.acornonline.com/graphics/products/zoom/XA2436.jpg', 'price': 35},
#             "Hoodie": {'image': 'https://underarmour.scene7.com/is/image/Underarmour/PS1357092-289_HF?rp=standard-0pad|pdpMainDesktop&scl=1&fmt=jpg&qlt=85&resMode=sharp2&cache=on,on&bgc=F0F0F0&wid=566&hei=708&size=566,708', 'price': 60},
#             "Shorts": {'image': 'https://media.cnn.com/api/v1/images/stellar/prod/mens-shorts-madewell-courdory.jpg?q=h_901,w_1600,x_0,y_0', 'price': 25},
#             "Chinos": {'image': 'https://www.themodestman.com/wp-content/uploads/2019/06/How-to-wear-chinos.jpeg', 'price': 55},
#             "Polo Shirt": {'image': 'https://cdn-prod.fluidconfigure.com/imagecomposer/generate/?view=front&recipe=1%2C-1%2C-1%2C-1%2C0%2C0%2C0%2C58%2C-1%2C28%2C12%2C-1%2C12%2C-1%2C-1%2C0%2C0%2C0%2C-1%2C-1%2C24%2C1%2C-1%2C0%2C0%2C-1%2C0%2C0%2C-1%2C-1%2C0%2C0%2C0%2C0%2C-1%2C-1%2C-1%2C-1%2C31%2C0%2C230%2C28%2C3%2C-1%2C0%2C-1%2C-1%2C-1%2C-1%2C0%2C-1%2C-1%2C-1%2C-1%2C0%2C-1%2C-1%2C-1%2C-1%2C0%2C-1%2C-1%2C-1%2C-1%2C0%2C31%2C0%2C0%2C7%2C0%2C5%2C0%2C0%2C0&apiKey=R8lp7_l6U7en-K1C4XrWRYgdjY4bPzVlk&workflow=prod&environment=prod&customerId=1563&productId=21561&configVersion=1686234349790&publishedTime=06%2F08%2F2023%2014%3A37%3A55&purpose=serverDisplay&format=jpg&trim=false&padding=0&scale=0.55&binary=true&quality=91&backgroundColor=%23ffffff', 'price': 30},
#             "Sweatshirt": {'image': 'https://mobile.yoox.com/images/items/12/12422474IW_14_f.jpg?impolicy=crop&width=387&height=490', 'price': 40},
#             "Cargo Pants": {'image': 'https://i5.walmartimages.com/asr/b786ae27-f2da-44a0-beed-ab8f7bcd7eaa.718e256e8b99a9c81bf12772472e0699.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF', 'price': 55},
#             "Jacket": {'image': 'https://cdn.shopify.com/s/files/1/0078/0333/8829/products/OR-Coldfront-Down-Hoodie-Mens_MADDER_1_460x@2x.png?v=1637263120', 'price': 70},
#             "Vest": {'image': 'https://cdni.llbean.net/is/image/wim/502429_461_41?scl=2', 'price': 35},
#             "Tank Top": {'image': 'https://target.scene7.com/is/image/Target/GUEST_99a9a499-cc80-40c1-8657-eceb59905675?wid=488&hei=488&fmt=pjpeg', 'price': 20},
#             "Cardigan": {'image': 'https://cdn11.bigcommerce.com/s-0f2c2/images/stencil/1280x1280/products/68/471/Mens-Modern-Alpaca-Golf-Cardigan-M168-004-F-Blue-AGS__36156.1541970319.gif?c=2', 'price': 45},
#             "Polo Dress": {'image': 'https://www.rlmedia.io/is/image/PoloGSI/s7-1356885_lifestyle?$plpDeskRF$', 'price': 50},
#             "Puffer Coat": {'image': 'https://www.differio.com/media/catalog/product/cache/0a727dd2e0a45cdfc82e01aae0d95d43/i/m/img_9168.jpg', 'price': 80},
#             "Jumper Dress": {'image': 'https://www.mynavyexchange.com/products/images/large/12839340_000.jpg', 'price': 40},
#             "Snapback Cap": {'image': 'https://www.toesonthenose.com/cdn/shop/products/TA558-NAT-side.jpg?v=1675453067', 'price': 20},
#             "Newsboy Cap": {'image': 'https://backwardglances.com/wp-content/uploads/2015/09/newsboy-cap-1.jpg', 'price': 25},
#             "Socks": {'image': 'https://chelseabootstore.com/wp-content/uploads/2018/08/The-Mens-Socks-Guide-Blog.jpg', 'price': 5},
#             "Underwear": {'image': 'https://n.nordstrommedia.com/id/sr3/cbfd9c98-8039-438b-b0da-314389fb71d0.jpeg?h=365&w=240&dpr=2', 'price': 10},
#             "Belt": {'image': 'https://thursdayboots.com/cdn/shop/products/1024x1024-Men-HeritageBelt-Brown-1.jpg?v=1593275111', 'price': 15},
#             "Scarf": {'image': 'https://www.baronboutique.com/wp-content/uploads/2021/06/satin-silk-scarf-col-406.jpg', 'price': 20},
#             "Beanie": {'image': 'https://products.blains.com/600/13/136100.jpg', 'price': 15},
#             "Gloves": {'image': 'https://glovesfortherapy.com/cdn/shop/products/merino_gloves_men_GTs.jpeg?v=1604316117', 'price': 10},
#             "Tie": {'image': 'https://www.thetiesite.com/media/catalog/product/cache/1/image/650x/040ec09b1e35df139433887a97daa66f/m/n/mn600-36.jpg', 'price': 15},
#             "Wallet": {'image': 'https://www.antorini.com/cdn/shop/products/black-wallet_29255841-f268-4844-8096-aad0dfef3b42_800x.jpg?v=1574930029', 'price': 25},
#             "Watch": {'image': 'https://i.ebayimg.com/images/g/JB8AAOSwfVFi14UL/s-l1200.webp', 'price': 150},
#         },
#         "Women's": {
#             "Dress": {'image': 'https://m.media-amazon.com/images/I/71h1vjKYXLL._AC_SL1500_.jpg', 'price': 40},
#             "Skirt": {'image': 'https://www.wilson.com/sites/default/files/Classic%20Pleated.jpg?', 'price': 25},
#             "Blouse": {'image': 'https://canary.contestimg.wish.com/api/webimage/5a938ad7da00377eca5ebeb4-large.jpg?cache_buster=6402432d0f4f51a8f92419467593a9d6', 'price': 30},
#             "Jumpsuit": {'image': 'https://www.travelandleisure.com/thmb/R0D2Er4tHhUHuafK-FbB4C9V7QM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/pink-queen-womens-jumpsuit-aa60bc42335a466db98c241a242ad151.jpg', 'price': 50},
#             "Romper": {'image': 'https://nypost.com/wp-content/uploads/sites/2/2022/03/71SStRHUfL._AC_UY879_.jpg', 'price': 45},
#             "Leggings": {'image': 'https://target.scene7.com/is/image/Target/GUEST_dcd993e9-02b6-4e6f-8316-afcb728a9e5f', 'price': 20},
#             "Capri Pants": {'image': 'https://m.media-amazon.com/images/I/611l26EUSyS._AC_UY1000_.jpg', 'price': 25},
#             "Maxi Dress": {'image': 'https://n.nordstrommedia.com/id/sr3/88432917-31f7-4969-99e5-0a80c51d033f.jpeg?h=365&w=240&dpr=2', 'price': 50},
#             "Crop Top": {'image': 'https://m.economictimes.com/thumb/msid-95693894,width-640,height-480,resizemode-7/mitaha-casual-western-stylish-crop-top.jpg', 'price': 20},
#             "Sweatshirt": {'image': 'https://www.instyle.com/thmb/zCqntmhND4buyGP-aKdq8i_sRwo=/fit-in/1500x933/filters:no_upscale():max_bytes(150000):strip_icc()/soly-hux-womens-letter-print-long-sleeve-casual-pullover-top-sweatshirt-e7a79a3d1d9345a1b7a02e19bc68cf52.jpg', 'price': 35},
#             "Pencil Skirt": {'image': 'https://i.etsystatic.com/27843024/r/il/9709e6/3233561867/il_fullxfull.3233561867_nl1g.jpg', 'price': 30},
#             "A-line Skirt": {'image': 'https://m.media-amazon.com/images/I/71JJrlvUafL._AC_UY1000_.jpg', 'price': 30},
#             "Poncho": {'image': 'https://images.fun.com/products/59967/1-1/pumpkin-womens-poncho-main.jpg', 'price': 45},
#             "Shawl": {'image': 'https://i.etsystatic.com/6235965/r/il/46ef0c/2410877222/il_fullxfull.2410877222_6oau.jpg', 'price': 40},
#             "Kimono": {'image': 'https://cdn.i-scmp.com/sites/default/files/styles/768x768/public/d8/images/canvas/2022/02/16/9697d283-5a63-4c2a-81ba-34a4096d2b1c_38d56931.jpg?itok=exh61L-p&v=1645019976', 'price': 50},
#             "Trench Dress": {'image': 'https://imperialhighlandsupplies.com/cdn/shop/products/Women_s-Winter-Wool-Dress-Coat-Double-Breasted-Pea-Coat-Long-Trench-Coat-camel.jpg?v=1673544712', 'price': 60},
#             "Tunic Dress": {'image': 'https://shopglobalpursuit.com/cdn/shop/products/coolibar-women-s-dresses-large-teal-bold-mosaic-coolibar-oceanside-tunic-dress-multiple-colors-14143417286723_1200x.png?v=1680794354', 'price': 35},
#             "Ruffled Blouse": {'image': 'https://i.pinimg.com/550x/64/01/9d/64019d5bd14687cb2bade8f4fdfd96bc.jpg', 'price': 30},
#             "Cold Shoulder Top": {'image': 'https://i5.walmartimages.com/asr/93febaab-ea66-437b-9698-e1981039711d.aa75cb1ebf800f8135bf8d726cf3c27f.jpeg', 'price': 25},
#             "Peplum Top": {'image': 'https://ak-media.theory.com/i/theory/TO_L072523R_U2Y_S0?$TO-pdp-large-desktop$', 'price': 25},
#             "Bandeau Top": {'image': 'https://i5.walmartimages.com/asr/a2fd7d8f-83ad-4243-b230-28fb114d803c.a80a1acca0816bee5ada59a16f9f9a7d.jpeg', 'price': 20},
#             "Fishnet Stockings": {'image': 'https://cdn-img.prettylittlething.com/b/3/c/a/b3ca64c3b442eca4608b6b065b0c90d10c944b4b_CLS2216_1.JPG', 'price': 15},
#             "Pashmina Scarf": {'image': 'https://i.etsystatic.com/8826469/r/il/0eb906/2602855293/il_570xN.2602855293_l4uv.jpg', 'price': 20},
#             "Earrings": {'image': 'https://n.nordstrommedia.com/id/sr3/5310a06a-f19f-40c4-a6fe-9b941b2af6d1.jpeg?h=365&w=240&dpr=2', 'price': 15},
#             "Necklace": {'image': 'https://m.media-amazon.com/images/I/71Sh+AoqBUL._AC_UY1100_.jpg', 'price': 20},
#             "Bracelet": {'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQaFTqM8Jy6m-m1WSUBb-9wx_JAOwijv3trw&usqp=CAU', 'price': 20},
#             "Ring": {'image': 'https://ie.pandora.net/dw/image/v2/BJRN_PRD/on/demandware.static/-/Sites-pandora-master-catalog/default/dwfb2f4011/productimages/singlepackshot/192611C01_RGB.jpg?sw=440&sh=440&sm=fit&sfrm=png&bgcolor=F5F5F5', 'price': 25},
#             "Purse": {'image': 'https://img.guess.com/image/upload/f_auto,q_auto:eco,fl_strip_profile,dpr_1.5,fl_advanced_resize,fl_progressive,w_392,c_scale/v1/NA/Style/ECOMM/AA878006-ORA-ALT2', 'price': 35},
#             "High Heels": {'image': 'https://i.ebayimg.com/images/g/y70AAOSw0-dgdk-A/s-l1200.webp', 'price': 40},
#             "Boots": {'image': 'https://media.istockphoto.com/id/990211696/photo/woman-wearing-black-boots.jpg?s=612x612&w=0&k=20&c=y09TC_ynxOxTcah3gtSj6U0JMkhl5tnIQ0ndqLTTYgg=', 'price': 60},
#         },
#         "Kids": {
#             "Onesie": {'image': 'https://pjammy.com/cdn/shop/products/SD4002USB-5_1800x.jpg?v=1670902901', 'price': 15},
#             "T-shirt": {'image': 'https://www.skhouston.com/pub/media/catalog/product/cache/249608ba4171d44d21805ed7657a13ae/t/s/tsk-003_tshirt_kid_blue.jpg', 'price': 10},
#             "Jeans": {'image': 'https://i5.walmartimages.com/asr/c2050be6-e261-4088-94e4-13a70380dbf4_1.5cb005d7fad91addd43ef2c0a554f2eb.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF', 'price': 20},
#             "Shorts": {'image': 'https://www.rei.com/media/d4d354d1-4756-4b94-b213-95da2bdf7c3a.jpg', 'price': 15},
#             "Dress": {'image': 'https://ae01.alicdn.com/kf/He5b1d3413d524880a27afae9ad4823d2U/2023-Formal-Summer-Dress-Baby-Girl-Flower-Kids-Dresses-For-Girls-Children-Clothing-Ball-Gown-Party.jpg', 'price': 20},
#             "Skirt": {'image': 'https://n.nordstrommedia.com/id/sr3/6b15a067-ee41-4966-a094-23dacc8fa3d9.jpeg?h=365&w=240&dpr=2', 'price': 15},
#             "Hoodie": {'image': 'https://i5.walmartimages.com/asr/c902cb5e-970d-4165-88f4-f8557a9cd3b4.fb35915da45fbb7b0e6ac2e06f1524a6.jpeg', 'price': 20},
#             "Pajamas": {'image': 'https://i5.walmartimages.com/asr/943d891b-937c-41f6-9c1c-6c7fac6616b2.a927fed753d5971009f0449cf71de3e4.jpeg', 'price': 15},
#             "Capri Pants": {'image': 'https://ae01.alicdn.com/kf/Sdb9078f5908c4655a497192fb154232ez/New-Kids-Boys-Cargo-Pants-Teens-Tactical-Pants-Children-Big-Pocket-Baggy-Trousers-Students-Casual-Sweatpants.jpg', 'price': 15},
#             "Sweatshirt": {'image': 'https://m.media-amazon.com/images/I/61WO7L-I-PL._AC_UY1000_.jpg', 'price': 20},
#             "Leggings": {'image': 'https://assets.theplace.com/image/upload/t_plp_img_m,f_auto,q_auto/v1/ecom/assets/products/gym/3040871/3040871_1692.png', 'price': 15},
#             "Polo Shirt": {'image': 'https://www.wholesaleschoolwear.com/v/vspfiles/photos/sspolokgsz-2.jpg?v-cache=1489656654', 'price': 15},
#             "Jumper Dress": {'image': 'https://cdn.modesens.com/product/22916009_8?w=400', 'price': 20},
#             "Trench Coat": {'image': 'https://cdn.modesens.com/media/84102629?w=400', 'price': 30},
#             "Tunic Dress": {'image': 'https://m.media-amazon.com/images/I/71V2U-frKjL._AC_UY1100_.jpg', 'price': 20},
#             "Ringer T-shirt": {'image': 'https://cdn.shopify.com/s/files/1/0706/8331/products/The-Machine-Maker-Ringer-White-Black.jpg?v=1657512176', 'price': 15},
#             "Joggers": {'image': 'https://richmanuniforms.com/wp-content/uploads/2022/06/IMG_0075.jpg', 'price': 20},
#             "Peplum Top": {'image': 'https://www.kidsblanks.com/wp-content/uploads/2022/10/lg3585c.jpg', 'price': 15},
#             "Tulle Skirt": {'image': 'https://i5.walmartimages.com/asr/0f20a9fd-3bd7-4eeb-b60d-a8c325e68fbe.2664adfbc7aa667e78a0d546ad0f2929.jpeg', 'price': 20},
#             "Palazzo Pants": {'image': 'https://www.thelittlebazaar.com/m/Kids/6889-aloha-cute-little-girls-cotton-palazzo-pants.jpg', 'price': 20},
#             "Cap Sleeve Top": {'image': 'https://ikatee.com/cdn/shop/products/P1090088_1400x.jpg?v=1650640618', 'price': 15},
#             "Bell-bottoms": {'image': 'https://media.rainpos.com/9518/IMG_5396.jpg', 'price': 20},
#             "Rain Boots": {'image': 'https://anyasreviews.com/wp-content/uploads/2022/02/Ten-Little-Affordable-Rain-Boots-Yellow-Cover.jpg', 'price': 25},
#             "School Uniform": {'image': 'https://parentingscience.com/wp-content/uploads/school-uniforms-cropped-from-Rawpixel.com-shutterstock-min.jpg', 'price': 30},
#             "Swimwear": {'image': 'https://m.media-amazon.com/images/I/41-igkeRE3L._AC_.jpg', 'price': 20},
#             "Flip Flops": {'image': 'https://sourpatchkids.com/media/catalog/product/cache/ec4522c5f46f94cf004b090e7d983f58/s/p/spk_flipflop_multi-kids_1.png', 'price': 10},
#             "Baseball Cap": {'image': 'https://m.media-amazon.com/images/I/71EzE7d6+UL._AC_UY1000_.jpg', 'price': 10},
#             "Bicycle Helmet": {'image': 'https://www.royalbabyglobal.com/cdn/shop/products/RoyalBaby-Dino-Helmet_1.webp?v=1650872243', 'price': 30},
#             "Backpack": {'image': 'https://m.media-amazon.com/images/I/91i3W-5QLIL._AC_UF894,1000_QL80_.jpg', 'price': 25},
#             "Sunglasses": {'image': 'https://shop.googlemerchandisestore.com/store/20160512512/assets/items/largeimages/GGOEGHGA118599.jpg', 'price': 15},
#         }
#     }

# create_items_and_reviews(clothing_items)

# _________________________________________________________
    # clothing_items = {
    #     "Men's": {
    #         "T-shirt": {'image': 'https://imgs.michaels.com/MAM/assets/1/5E3C12034D34434F8A9BAAFDDF0F8E1B/img/617E940D442246D4AA2F229D24F20BAE/10707691_1.jpg', 'price': 20},
    #         "Jeans": {'image': 'https://m.media-amazon.com/images/I/81qCSIMK6QL._AC_UF894,1000_QL80_.jpg', 'price': 50},
    #         "Dress Shirt": {'image': 'https://www.amedeoexclusive.com/cdn/shop/products/AEBD8054_2_1200x.progressive.jpg?v=1598429697', 'price': 30},
    #         "Suit": {'image': 'https://i.pinimg.com/originals/98/3f/55/983f55888eb0ca318d79dd1515ba3498.jpg', 'price': 100},
    #         "Blazer": {'image': 'https://m.media-amazon.com/images/I/61AP9GoC+jL.jpg', 'price': 80},
    #         "Sweater": {'image': 'https://www.acornonline.com/graphics/products/zoom/XA2436.jpg', 'price': 35},
    #         "Hoodie": {'image': 'https://underarmour.scene7.com/is/image/Underarmour/PS1357092-289_HF?rp=standard-0pad|pdpMainDesktop&scl=1&fmt=jpg&qlt=85&resMode=sharp2&cache=on,on&bgc=F0F0F0&wid=566&hei=708&size=566,708', 'price': 60},
    #         "Shorts": {'image': 'https://media.cnn.com/api/v1/images/stellar/prod/mens-shorts-madewell-courdory.jpg?q=h_901,w_1600,x_0,y_0', 'price': 25},
    #         "Chinos": {'image': 'https://www.themodestman.com/wp-content/uploads/2019/06/How-to-wear-chinos.jpeg', 'price': 55},
    #         "Polo Shirt": {'image': 'https://cdn-prod.fluidconfigure.com/imagecomposer/generate/?view=front&recipe=1%2C-1%2C-1%2C-1%2C0%2C0%2C0%2C58%2C-1%2C28%2C12%2C-1%2C12%2C-1%2C-1%2C0%2C0%2C0%2C-1%2C-1%2C24%2C1%2C-1%2C0%2C0%2C-1%2C0%2C0%2C-1%2C-1%2C0%2C0%2C0%2C0%2C-1%2C-1%2C-1%2C-1%2C31%2C0%2C230%2C28%2C3%2C-1%2C0%2C-1%2C-1%2C-1%2C-1%2C0%2C-1%2C-1%2C-1%2C-1%2C0%2C-1%2C-1%2C-1%2C-1%2C0%2C-1%2C-1%2C-1%2C-1%2C0%2C31%2C0%2C0%2C7%2C0%2C5%2C0%2C0%2C0&apiKey=R8lp7_l6U7en-K1C4XrWRYgdjY4bPzVlk&workflow=prod&environment=prod&customerId=1563&productId=21561&configVersion=1686234349790&publishedTime=06%2F08%2F2023%2014%3A37%3A55&purpose=serverDisplay&format=jpg&trim=false&padding=0&scale=0.55&binary=true&quality=91&backgroundColor=%23ffffff', 'price': 30},
    #         "Sweatshirt": {'image': 'https://mobile.yoox.com/images/items/12/12422474IW_14_f.jpg?impolicy=crop&width=387&height=490', 'price': 40},
    #         "Cargo Pants": {'image': 'https://i5.walmartimages.com/asr/b786ae27-f2da-44a0-beed-ab8f7bcd7eaa.718e256e8b99a9c81bf12772472e0699.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF', 'price': 55},
    #         "Jacket": {'image': 'https://cdn.shopify.com/s/files/1/0078/0333/8829/products/OR-Coldfront-Down-Hoodie-Mens_MADDER_1_460x@2x.png?v=1637263120', 'price': 70},
    #         "Vest": {'image': 'https://cdni.llbean.net/is/image/wim/502429_461_41?scl=2', 'price': 35},
    #         "Tank Top": {'image': 'https://target.scene7.com/is/image/Target/GUEST_99a9a499-cc80-40c1-8657-eceb59905675?wid=488&hei=488&fmt=pjpeg', 'price': 20},
    #         "Cardigan": {'image': 'https://cdn11.bigcommerce.com/s-0f2c2/images/stencil/1280x1280/products/68/471/Mens-Modern-Alpaca-Golf-Cardigan-M168-004-F-Blue-AGS__36156.1541970319.gif?c=2', 'price': 45},
    #         "Polo Dress": {'image': 'https://www.rlmedia.io/is/image/PoloGSI/s7-1356885_lifestyle?$plpDeskRF$', 'price': 50},
    #         "Puffer Coat": {'image': 'https://www.differio.com/media/catalog/product/cache/0a727dd2e0a45cdfc82e01aae0d95d43/i/m/img_9168.jpg', 'price': 80},
    #         "Jumper Dress": {'image': 'https://www.mynavyexchange.com/products/images/large/12839340_000.jpg', 'price': 40},
    #         "Snapback Cap": {'image': 'https://www.toesonthenose.com/cdn/shop/products/TA558-NAT-side.jpg?v=1675453067', 'price': 20},
    #         "Newsboy Cap": {'image': 'https://backwardglances.com/wp-content/uploads/2015/09/newsboy-cap-1.jpg', 'price': 25},
    #         "Socks": {'image': 'https://chelseabootstore.com/wp-content/uploads/2018/08/The-Mens-Socks-Guide-Blog.jpg', 'price': 5},
    #         "Underwear": {'image': 'https://n.nordstrommedia.com/id/sr3/cbfd9c98-8039-438b-b0da-314389fb71d0.jpeg?h=365&w=240&dpr=2', 'price': 10},
    #         "Belt": {'image': 'https://thursdayboots.com/cdn/shop/products/1024x1024-Men-HeritageBelt-Brown-1.jpg?v=1593275111', 'price': 15},
    #         "Scarf": {'image': 'https://www.baronboutique.com/wp-content/uploads/2021/06/satin-silk-scarf-col-406.jpg', 'price': 20},
    #         "Beanie": {'image': 'https://products.blains.com/600/13/136100.jpg', 'price': 15},
    #         "Gloves": {'image': 'https://glovesfortherapy.com/cdn/shop/products/merino_gloves_men_GTs.jpeg?v=1604316117', 'price': 10},
    #         "Tie": {'image': 'https://www.thetiesite.com/media/catalog/product/cache/1/image/650x/040ec09b1e35df139433887a97daa66f/m/n/mn600-36.jpg', 'price': 15},
    #         "Wallet": {'image': 'https://www.antorini.com/cdn/shop/products/black-wallet_29255841-f268-4844-8096-aad0dfef3b42_800x.jpg?v=1574930029', 'price': 25},
    #         "Watch": {'image': 'https://i.ebayimg.com/images/g/JB8AAOSwfVFi14UL/s-l1200.webp', 'price': 150},
    #     },
    #     "Women's": {
    #         "Dress": {'image': 'https://m.media-amazon.com/images/I/71h1vjKYXLL._AC_SL1500_.jpg', 'price': 40},
    #         "Skirt": {'image': 'https://www.wilson.com/sites/default/files/Classic%20Pleated.jpg?', 'price': 25},
    #         "Blouse": {'image': 'https://canary.contestimg.wish.com/api/webimage/5a938ad7da00377eca5ebeb4-large.jpg?cache_buster=6402432d0f4f51a8f92419467593a9d6', 'price': 30},
    #         "Jumpsuit": {'image': 'https://www.travelandleisure.com/thmb/R0D2Er4tHhUHuafK-FbB4C9V7QM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/pink-queen-womens-jumpsuit-aa60bc42335a466db98c241a242ad151.jpg', 'price': 50},
    #         "Romper": {'image': 'https://nypost.com/wp-content/uploads/sites/2/2022/03/71SStRHUfL._AC_UY879_.jpg', 'price': 45},
    #         "Leggings": {'image': 'https://target.scene7.com/is/image/Target/GUEST_dcd993e9-02b6-4e6f-8316-afcb728a9e5f', 'price': 20},
    #         "Capri Pants": {'image': 'https://m.media-amazon.com/images/I/611l26EUSyS._AC_UY1000_.jpg', 'price': 25},
    #         "Maxi Dress": {'image': 'https://n.nordstrommedia.com/id/sr3/88432917-31f7-4969-99e5-0a80c51d033f.jpeg?h=365&w=240&dpr=2', 'price': 50},
    #         "Crop Top": {'image': 'https://m.economictimes.com/thumb/msid-95693894,width-640,height-480,resizemode-7/mitaha-casual-western-stylish-crop-top.jpg', 'price': 20},
    #         "Sweatshirt": {'image': 'https://www.instyle.com/thmb/zCqntmhND4buyGP-aKdq8i_sRwo=/fit-in/1500x933/filters:no_upscale():max_bytes(150000):strip_icc()/soly-hux-womens-letter-print-long-sleeve-casual-pullover-top-sweatshirt-e7a79a3d1d9345a1b7a02e19bc68cf52.jpg', 'price': 35},
    #         "Pencil Skirt": {'image': 'https://i.etsystatic.com/27843024/r/il/9709e6/3233561867/il_fullxfull.3233561867_nl1g.jpg', 'price': 30},
    #         "A-line Skirt": {'image': 'https://m.media-amazon.com/images/I/71JJrlvUafL._AC_UY1000_.jpg', 'price': 30},
    #         "Poncho": {'image': 'https://images.fun.com/products/59967/1-1/pumpkin-womens-poncho-main.jpg', 'price': 45},
    #         "Shawl": {'image': 'https://i.etsystatic.com/6235965/r/il/46ef0c/2410877222/il_fullxfull.2410877222_6oau.jpg', 'price': 40},
    #         "Kimono": {'image': 'https://cdn.i-scmp.com/sites/default/files/styles/768x768/public/d8/images/canvas/2022/02/16/9697d283-5a63-4c2a-81ba-34a4096d2b1c_38d56931.jpg?itok=exh61L-p&v=1645019976', 'price': 50},
    #         "Trench Dress": {'image': 'https://imperialhighlandsupplies.com/cdn/shop/products/Women_s-Winter-Wool-Dress-Coat-Double-Breasted-Pea-Coat-Long-Trench-Coat-camel.jpg?v=1673544712', 'price': 60},
    #         "Tunic Dress": {'image': 'https://shopglobalpursuit.com/cdn/shop/products/coolibar-women-s-dresses-large-teal-bold-mosaic-coolibar-oceanside-tunic-dress-multiple-colors-14143417286723_1200x.png?v=1680794354', 'price': 35},
    #         "Ruffled Blouse": {'image': 'https://i.pinimg.com/550x/64/01/9d/64019d5bd14687cb2bade8f4fdfd96bc.jpg', 'price': 30},
    #         "Cold Shoulder Top": {'image': 'https://i5.walmartimages.com/asr/93febaab-ea66-437b-9698-e1981039711d.aa75cb1ebf800f8135bf8d726cf3c27f.jpeg', 'price': 25},
    #         "Peplum Top": {'image': 'https://ak-media.theory.com/i/theory/TO_L072523R_U2Y_S0?$TO-pdp-large-desktop$', 'price': 25},
    #         "Bandeau Top": {'image': 'https://i5.walmartimages.com/asr/a2fd7d8f-83ad-4243-b230-28fb114d803c.a80a1acca0816bee5ada59a16f9f9a7d.jpeg', 'price': 20},
    #         "Fishnet Stockings": {'image': 'https://cdn-img.prettylittlething.com/b/3/c/a/b3ca64c3b442eca4608b6b065b0c90d10c944b4b_CLS2216_1.JPG', 'price': 15},
    #         "Pashmina Scarf": {'image': 'https://i.etsystatic.com/8826469/r/il/0eb906/2602855293/il_570xN.2602855293_l4uv.jpg', 'price': 20},
    #         "Earrings": {'image': 'https://n.nordstrommedia.com/id/sr3/5310a06a-f19f-40c4-a6fe-9b941b2af6d1.jpeg?h=365&w=240&dpr=2', 'price': 15},
    #         "Necklace": {'image': 'https://m.media-amazon.com/images/I/71Sh+AoqBUL._AC_UY1100_.jpg', 'price': 20},
    #         "Bracelet": {'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQaFTqM8Jy6m-m1WSUBb-9wx_JAOwijv3trw&usqp=CAU', 'price': 20},
    #         "Ring": {'image': 'https://ie.pandora.net/dw/image/v2/BJRN_PRD/on/demandware.static/-/Sites-pandora-master-catalog/default/dwfb2f4011/productimages/singlepackshot/192611C01_RGB.jpg?sw=440&sh=440&sm=fit&sfrm=png&bgcolor=F5F5F5', 'price': 25},
    #         "Purse": {'image': 'https://img.guess.com/image/upload/f_auto,q_auto:eco,fl_strip_profile,dpr_1.5,fl_advanced_resize,fl_progressive,w_392,c_scale/v1/NA/Style/ECOMM/AA878006-ORA-ALT2', 'price': 35},
    #         "High Heels": {'image': 'https://i.ebayimg.com/images/g/y70AAOSw0-dgdk-A/s-l1200.webp', 'price': 40},
    #         "Boots": {'image': 'https://media.istockphoto.com/id/990211696/photo/woman-wearing-black-boots.jpg?s=612x612&w=0&k=20&c=y09TC_ynxOxTcah3gtSj6U0JMkhl5tnIQ0ndqLTTYgg=', 'price': 60},
    #     },
    #     "Kids": {
    #         "Onesie": {'image': 'https://pjammy.com/cdn/shop/products/SD4002USB-5_1800x.jpg?v=1670902901', 'price': 15},
    #         "T-shirt": {'image': 'https://www.skhouston.com/pub/media/catalog/product/cache/249608ba4171d44d21805ed7657a13ae/t/s/tsk-003_tshirt_kid_blue.jpg', 'price': 10},
    #         "Jeans": {'image': 'https://i5.walmartimages.com/asr/c2050be6-e261-4088-94e4-13a70380dbf4_1.5cb005d7fad91addd43ef2c0a554f2eb.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF', 'price': 20},
    #         "Shorts": {'image': 'https://www.rei.com/media/d4d354d1-4756-4b94-b213-95da2bdf7c3a.jpg', 'price': 15},
    #         "Dress": {'image': 'https://ae01.alicdn.com/kf/He5b1d3413d524880a27afae9ad4823d2U/2023-Formal-Summer-Dress-Baby-Girl-Flower-Kids-Dresses-For-Girls-Children-Clothing-Ball-Gown-Party.jpg', 'price': 20},
    #         "Skirt": {'image': 'https://n.nordstrommedia.com/id/sr3/6b15a067-ee41-4966-a094-23dacc8fa3d9.jpeg?h=365&w=240&dpr=2', 'price': 15},
    #         "Hoodie": {'image': 'https://i5.walmartimages.com/asr/c902cb5e-970d-4165-88f4-f8557a9cd3b4.fb35915da45fbb7b0e6ac2e06f1524a6.jpeg', 'price': 20},
    #         "Pajamas": {'image': 'https://i5.walmartimages.com/asr/943d891b-937c-41f6-9c1c-6c7fac6616b2.a927fed753d5971009f0449cf71de3e4.jpeg', 'price': 15},
    #         "Capri Pants": {'image': 'https://ae01.alicdn.com/kf/Sdb9078f5908c4655a497192fb154232ez/New-Kids-Boys-Cargo-Pants-Teens-Tactical-Pants-Children-Big-Pocket-Baggy-Trousers-Students-Casual-Sweatpants.jpg', 'price': 15},
    #         "Sweatshirt": {'image': 'https://m.media-amazon.com/images/I/61WO7L-I-PL._AC_UY1000_.jpg', 'price': 20},
    #         "Leggings": {'image': 'https://assets.theplace.com/image/upload/t_plp_img_m,f_auto,q_auto/v1/ecom/assets/products/gym/3040871/3040871_1692.png', 'price': 15},
    #         "Polo Shirt": {'image': 'https://www.wholesaleschoolwear.com/v/vspfiles/photos/sspolokgsz-2.jpg?v-cache=1489656654', 'price': 15},
    #         "Jumper Dress": {'image': 'https://cdn.modesens.com/product/22916009_8?w=400', 'price': 20},
    #         "Trench Coat": {'image': 'https://cdn.modesens.com/media/84102629?w=400', 'price': 30},
    #         "Tunic Dress": {'image': 'https://m.media-amazon.com/images/I/71V2U-frKjL._AC_UY1100_.jpg', 'price': 20},
    #         "Ringer T-shirt": {'image': 'https://cdn.shopify.com/s/files/1/0706/8331/products/The-Machine-Maker-Ringer-White-Black.jpg?v=1657512176', 'price': 15},
    #         "Joggers": {'image': 'https://richmanuniforms.com/wp-content/uploads/2022/06/IMG_0075.jpg', 'price': 20},
    #         "Peplum Top": {'image': 'https://www.kidsblanks.com/wp-content/uploads/2022/10/lg3585c.jpg', 'price': 15},
    #         "Tulle Skirt": {'image': 'https://i5.walmartimages.com/asr/0f20a9fd-3bd7-4eeb-b60d-a8c325e68fbe.2664adfbc7aa667e78a0d546ad0f2929.jpeg', 'price': 20},
    #         "Palazzo Pants": {'image': 'https://www.thelittlebazaar.com/m/Kids/6889-aloha-cute-little-girls-cotton-palazzo-pants.jpg', 'price': 20},
    #         "Cap Sleeve Top": {'image': 'https://ikatee.com/cdn/shop/products/P1090088_1400x.jpg?v=1650640618', 'price': 15},
    #         "Bell-bottoms": {'image': 'https://media.rainpos.com/9518/IMG_5396.jpg', 'price': 20},
    #         "Rain Boots": {'image': 'https://anyasreviews.com/wp-content/uploads/2022/02/Ten-Little-Affordable-Rain-Boots-Yellow-Cover.jpg', 'price': 25},
    #         "School Uniform": {'image': 'https://parentingscience.com/wp-content/uploads/school-uniforms-cropped-from-Rawpixel.com-shutterstock-min.jpg', 'price': 30},
    #         "Swimwear": {'image': 'https://m.media-amazon.com/images/I/41-igkeRE3L._AC_.jpg', 'price': 20},
    #         "Flip Flops": {'image': 'https://sourpatchkids.com/media/catalog/product/cache/ec4522c5f46f94cf004b090e7d983f58/s/p/spk_flipflop_multi-kids_1.png', 'price': 10},
    #         "Baseball Cap": {'image': 'https://m.media-amazon.com/images/I/71EzE7d6+UL._AC_UY1000_.jpg', 'price': 10},
    #         "Bicycle Helmet": {'image': 'https://www.royalbabyglobal.com/cdn/shop/products/RoyalBaby-Dino-Helmet_1.webp?v=1650872243', 'price': 30},
    #         "Backpack": {'image': 'https://m.media-amazon.com/images/I/91i3W-5QLIL._AC_UF894,1000_QL80_.jpg', 'price': 25},
    #         "Sunglasses": {'image': 'https://shop.googlemerchandisestore.com/store/20160512512/assets/items/largeimages/GGOEGHGA118599.jpg', 'price': 15},
    #     }
    # }





