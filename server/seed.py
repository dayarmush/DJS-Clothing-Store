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
        "T-shirt", "Jeans", "Dress", "Sweater", "Hoodie", "Shorts", "Skirt",
        "Blouse", "Blazer", "Suit", "Coat", "Jacket", "Vest", "Tank top", "Cardigan",
        "Jumpsuit", "Romper", "Polo shirt", "Sweatshirt", "Leggings", "Cargo pants",
        "Capri pants", "Overalls", "Pajamas", "Bathrobe", "Onesie", "Trench coat",
        "Peacoat", "Kimono", "Sarong", "Maxi dress", "Mini skirt", "Midi dress",
        "Crop top", "Chinos", "Flannel shirt", "Camisole", "Halter top", "Poncho",
        "Shawl", "Kaftan", "Anorak", "Windbreaker", "Raincoat", "Parka",
        "Turtleneck", "Polo dress", "Sun dress", "Tuxedo", "Tuxedo dress",
        "Ruffled blouse", "Pencil skirt", "A-line skirt", "Culottes", "Cargo shorts",
        "Athletic shorts", "Denim jacket", "Leather jacket", "Suede jacket",
        "Down jacket", "Kimono jacket", "Off-the-shoulder top", "Button-up shirt",
        "Puffer coat", "Sheath dress", "Jeggings", "Harem pants", "Capris",
        "Cap sleeve top", "Bell-bottoms", "Jumper dress", "Bandeau top",
        "Fishnet stockings", "Pashmina scarf", "Ascot tie", "Headband",
        "Leg warmers", "Newsboy cap", "Beret", "Bow tie", "Necktie",
        "Pocket square", "Cravat", "Bowler hat", "Beanie", "Fedora",
        "Visor", "Snapback cap", "Boater hat", "Newsboy cap",
        "Trench dress", "Tunic dress", "Cold shoulder top", "Ringer T-shirt", "Joggers",
        "Biker jacket", "Chore coat", "Peplum top", "Tulle skirt", "Palazzo pants"
    ]

    image_urls = [
    # Men's
    'https://imgs.michaels.com/MAM/assets/1/5E3C12034D34434F8A9BAAFDDF0F8E1B/img/617E940D442246D4AA2F229D24F20BAE/10707691_1.jpg',
    'https://m.media-amazon.com/images/I/81qCSIMK6QL._AC_UF894,1000_QL80_.jpg',
    'https://www.amedeoexclusive.com/cdn/shop/products/AEBD8054_2_1200x.progressive.jpg?v=1598429697',
    'https://i.pinimg.com/originals/98/3f/55/983f55888eb0ca318d79dd1515ba3498.jpg',
    'https://m.media-amazon.com/images/I/61AP9GoC+jL.jpg',
    'https://www.acornonline.com/graphics/products/zoom/XA2436.jpg',
    'https://underarmour.scene7.com/is/image/Underarmour/PS1357092-289_HF?rp=standard-0pad|pdpMainDesktop&scl=1&fmt=jpg&qlt=85&resMode=sharp2&cache=on,on&bgc=F0F0F0&wid=566&hei=708&size=566,708',
    'https://media.cnn.com/api/v1/images/stellar/prod/mens-shorts-madewell-courdory.jpg?q=h_901,w_1600,x_0,y_0',
    'https://www.themodestman.com/wp-content/uploads/2019/06/How-to-wear-chinos.jpeg',
    'https://cdn-prod.fluidconfigure.com/imagecomposer/generate/?view=front&recipe=1%2C-1%2C-1%2C-1%2C0%2C0%2C0%2C58%2C-1%2C28%2C12%2C-1%2C12%2C-1%2C-1%2C0%2C0%2C0%2C-1%2C-1%2C24%2C1%2C-1%2C0%2C0%2C-1%2C0%2C0%2C-1%2C-1%2C0%2C0%2C0%2C0%2C-1%2C-1%2C-1%2C-1%2C31%2C0%2C230%2C28%2C3%2C-1%2C0%2C-1%2C-1%2C-1%2C-1%2C0%2C-1%2C-1%2C-1%2C-1%2C0%2C-1%2C-1%2C-1%2C-1%2C0%2C31%2C0%2C0%2C7%2C0%2C5%2C0%2C0%2C0&apiKey=R8lp7_l6U7en-K1C4XrWRYgdjY4bPzVlk&workflow=prod&environment=prod&customerId=1563&productId=21561&configVersion=1686234349790&publishedTime=06%2F08%2F2023%2014%3A37%3A55&purpose=serverDisplay&format=jpg&trim=false&padding=0&scale=0.55&binary=true&quality=91&backgroundColor=%23ffffff',
    'https://mobile.yoox.com/images/items/12/12422474IW_14_f.jpg?impolicy=crop&width=387&height=490',
    'https://i5.walmartimages.com/asr/b786ae27-f2da-44a0-beed-ab8f7bcd7eaa.718e256e8b99a9c81bf12772472e0699.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF',
    'https://cdn.shopify.com/s/files/1/0078/0333/8829/products/OR-Coldfront-Down-Hoodie-Mens_MADDER_1_460x@2x.png?v=1637263120',
    'https://cdni.llbean.net/is/image/wim/502429_461_41?scl=2',
    'https://target.scene7.com/is/image/Target/GUEST_99a9a499-cc80-40c1-8657-eceb59905675?wid=488&hei=488&fmt=pjpeg',
    'https://cdn11.bigcommerce.com/s-0f2c2/images/stencil/1280x1280/products/68/471/Mens-Modern-Alpaca-Golf-Cardigan-M168-004-F-Blue-AGS__36156.1541970319.gif?c=2',
    'https://www.rlmedia.io/is/image/PoloGSI/s7-1356885_lifestyle?$plpDeskRF$',
    'https://www.differio.com/media/catalog/product/cache/0a727dd2e0a45cdfc82e01aae0d95d43/i/m/img_9168.jpg',
    'https://www.mynavyexchange.com/products/images/large/12839340_000.jpg',
    'https://www.toesonthenose.com/cdn/shop/products/TA558-NAT-side.jpg?v=1675453067',
    'https://backwardglances.com/wp-content/uploads/2015/09/newsboy-cap-1.jpg',
    'https://chelseabootstore.com/wp-content/uploads/2018/08/The-Mens-Socks-Guide-Blog.jpg',
    'https://n.nordstrommedia.com/id/sr3/cbfd9c98-8039-438b-b0da-314389fb71d0.jpeg?h=365&w=240&dpr=2',
    'https://thursdayboots.com/cdn/shop/products/1024x1024-Men-HeritageBelt-Brown-1.jpg?v=1593275111',
    'https://www.baronboutique.com/wp-content/uploads/2021/06/satin-silk-scarf-col-406.jpg',
    'https://products.blains.com/600/13/136100.jpg',
    'https://glovesfortherapy.com/cdn/shop/products/merino_gloves_men_GTs.jpeg?v=1604316117',
    'https://www.thetiesite.com/media/catalog/product/cache/1/image/650x/040ec09b1e35df139433887a97daa66f/m/n/mn600-36.jpg',
    'https://www.antorini.com/cdn/shop/products/black-wallet_29255841-f268-4844-8096-aad0dfef3b42_800x.jpg?v=1574930029',
    'https://i.ebayimg.com/images/g/JB8AAOSwfVFi14UL/s-l1200.webp',

    # Women's
    'https://m.media-amazon.com/images/I/71h1vjKYXLL._AC_SL1500_.jpg',
    'https://www.wilson.com/sites/default/files/Classic%20Pleated.jpg?',
    'https://canary.contestimg.wish.com/api/webimage/5a938ad7da00377eca5ebeb4-large.jpg?cache_buster=6402432d0f4f51a8f92419467593a9d6',
    'https://www.travelandleisure.com/thmb/R0D2Er4tHhUHuafK-FbB4C9V7QM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/pink-queen-womens-jumpsuit-aa60bc42335a466db98c241a242ad151.jpg',
    'https://nypost.com/wp-content/uploads/sites/2/2022/03/71SStRHUfL._AC_UY879_.jpg',
    'https://target.scene7.com/is/image/Target/GUEST_dcd993e9-02b6-4e6f-8316-afcb728a9e5f',
    'https://m.media-amazon.com/images/I/611l26EUSyS._AC_UY1000_.jpg',
    'https://n.nordstrommedia.com/id/sr3/88432917-31f7-4969-99e5-0a80c51d033f.jpeg?h=365&w=240&dpr=2',
    'https://m.economictimes.com/thumb/msid-95693894,width-640,height-480,resizemode-7/mitaha-casual-western-stylish-crop-top.jpg',
    'https://www.instyle.com/thmb/zCqntmhND4buyGP-aKdq8i_sRwo=/fit-in/1500x933/filters:no_upscale():max_bytes(150000):strip_icc()/soly-hux-womens-letter-print-long-sleeve-casual-pullover-top-sweatshirt-e7a79a3d1d9345a1b7a02e19bc68cf52.jpg',
    'https://i.etsystatic.com/27843024/r/il/9709e6/3233561867/il_fullxfull.3233561867_nl1g.jpg',
    'https://m.media-amazon.com/images/I/71JJrlvUafL._AC_UY1000_.jpg',
    'https://images.fun.com/products/59967/1-1/pumpkin-womens-poncho-main.jpg',
    'https://i.etsystatic.com/6235965/r/il/46ef0c/2410877222/il_fullxfull.2410877222_6oau.jpg',
    'https://cdn.i-scmp.com/sites/default/files/styles/768x768/public/d8/images/canvas/2022/02/16/9697d283-5a63-4c2a-81ba-34a4096d2b1c_38d56931.jpg?itok=exh61L-p&v=1645019976',
    'https://imperialhighlandsupplies.com/cdn/shop/products/Women_s-Winter-Wool-Dress-Coat-Double-Breasted-Pea-Coat-Long-Trench-Coat-camel.jpg?v=1673544712',
    'https://shopglobalpursuit.com/cdn/shop/products/coolibar-women-s-dresses-large-teal-bold-mosaic-coolibar-oceanside-tunic-dress-multiple-colors-14143417286723_1200x.png?v=1680794354',
    'https://i.pinimg.com/550x/64/01/9d/64019d5bd14687cb2bade8f4fdfd96bc.jpg',
    'https://i5.walmartimages.com/asr/93febaab-ea66-437b-9698-e1981039711d.aa75cb1ebf800f8135bf8d726cf3c27f.jpeg',
    'https://ak-media.theory.com/i/theory/TO_L072523R_U2Y_S0?$TO-pdp-large-desktop$',
    'https://i5.walmartimages.com/asr/a2fd7d8f-83ad-4243-b230-28fb114d803c.a80a1acca0816bee5ada59a16f9f9a7d.jpeg',
    'https://cdn-img.prettylittlething.com/b/3/c/a/b3ca64c3b442eca4608b6b065b0c90d10c944b4b_CLS2216_1.JPG',
    'https://i.etsystatic.com/8826469/r/il/0eb906/2602855293/il_570xN.2602855293_l4uv.jpg',
    'https://n.nordstrommedia.com/id/sr3/5310a06a-f19f-40c4-a6fe-9b941b2af6d1.jpeg?h=365&w=240&dpr=2',
    'https://m.media-amazon.com/images/I/71Sh+AoqBUL._AC_UY1100_.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQaFTqM8Jy6m-m1WSUBb-9wx_JAOwijv3trw&usqp=CAU',
    'https://ie.pandora.net/dw/image/v2/BJRN_PRD/on/demandware.static/-/Sites-pandora-master-catalog/default/dwfb2f4011/productimages/singlepackshot/192611C01_RGB.jpg?sw=440&sh=440&sm=fit&sfrm=png&bgcolor=F5F5F5',
    'https://img.guess.com/image/upload/f_auto,q_auto:eco,fl_strip_profile,dpr_1.5,fl_advanced_resize,fl_progressive,w_392,c_scale/v1/NA/Style/ECOMM/AA878006-ORA-ALT2',
    'https://i.ebayimg.com/images/g/y70AAOSw0-dgdk-A/s-l1200.webp',

    # Kids
    'https://pjammy.com/cdn/shop/products/SD4002USB-5_1800x.jpg?v=1670902901',
    'https://www.skhouston.com/pub/media/catalog/product/cache/249608ba4171d44d21805ed7657a13ae/t/s/tsk-003_tshirt_kid_blue.jpg',
    'https://i5.walmartimages.com/asr/c2050be6-e261-4088-94e4-13a70380dbf4_1.5cb005d7fad91addd43ef2c0a554f2eb.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF',
    'https://www.rei.com/media/d4d354d1-4756-4b94-b213-95da2bdf7c3a.jpg',
    'https://ae01.alicdn.com/kf/He5b1d3413d524880a27afae9ad4823d2U/2023-Formal-Summer-Dress-Baby-Girl-Flower-Kids-Dresses-For-Girls-Children-Clothing-Ball-Gown-Party.jpg',
    'https://n.nordstrommedia.com/id/sr3/6b15a067-ee41-4966-a094-23dacc8fa3d9.jpeg?h=365&w=240&dpr=2',
    'https://i5.walmartimages.com/asr/c902cb5e-970d-4165-88f4-f8557a9cd3b4.fb35915da45fbb7b0e6ac2e06f1524a6.jpeg',
    'https://i5.walmartimages.com/asr/943d891b-937c-41f6-9c1c-6c7fac6616b2.a927fed753d5971009f0449cf71de3e4.jpeg',
    'https://ae01.alicdn.com/kf/Sdb9078f5908c4655a497192fb154232ez/New-Kids-Boys-Cargo-Pants-Teens-Tactical-Pants-Children-Big-Pocket-Baggy-Trousers-Students-Casual-Sweatpants.jpg',
    'https://m.media-amazon.com/images/I/61WO7L-I-PL._AC_UY1000_.jpg',
    'https://assets.theplace.com/image/upload/t_plp_img_m,f_auto,q_auto/v1/ecom/assets/products/gym/3040871/3040871_1692.png',
    'https://www.wholesaleschoolwear.com/v/vspfiles/photos/sspolokgsz-2.jpg',
    'https://cdn.modesens.com/product/22916009_8?w=400',
    'https://m.media-amazon.com/images/I/71V2U-frKjL._AC_UY1100_.jpg',
    'https://cdn.shopify.com/s/files/1/0706/8331/products/The-Machine-Maker-Ringer-White-Black.jpg?v=1657512176',
    'https://richmanuniforms.com/wp-content/uploads/2022/06/IMG_0075.jpg',
    'https://www.kidsblanks.com/wp-content/uploads/2022/10/lg3585c.jpg',
    'https://i5.walmartimages.com/asr/0f20a9fd-3bd7-4eeb-b60d-a8c325e68fbe.2664adfbc7aa667e78a0d546ad0f2929.jpeg',
    'https://www.thelittlebazaar.com/m/Kids/6889-aloha-cute-little-girls-cotton-palazzo-pants.jpg',
    'https://ikatee.com/cdn/shop/products/P1090088_1400x.jpg?v=1650640618',
    'https://media.rainpos.com/9518/IMG_5396.jpg',
    'https://anyasreviews.com/wp-content/uploads/2022/02/Ten-Little-Affordable-Rain-Boots-Yellow-Cover.jpg',
    'https://parentingscience.com/wp-content/uploads/school-uniforms-cropped-from-Rawpixel.com-shutterstock-min.jpg',
    'https://m.media-amazon.com/images/I/41-igkeRE3L._AC_.jpg',
    'https://sourpatchkids.com/media/catalog/product/cache/ec4522c5f46f94cf004b090e7d983f58/s/p/spk_flipflop_multi-kids_1.png',
    'https://www.royalbabyglobal.com/cdn/shop/products/RoyalBaby-Dino-Helmet_1.webp?v=1650872243',
    'https://m.media-amazon.com/images/I/91i3W-5QLIL._AC_UF894,1000_QL80_.jpg',
    'https://shop.googlemerchandisestore.com/store/20160512512/assets/items/largeimages/GGOEGHGA118599.jpg'
]

    items = []
    for i in range(100):
        item = Item(
            name=rc(clothing_items),
            image=rc(image_urls),
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

