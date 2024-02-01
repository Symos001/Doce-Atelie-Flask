from app import db


class User(db.Model):
    __tablename__ ="users"
    
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique=True)
    password = db.Column(db.String)
    name= db.Column(db.String)
    email=db.Column(db.String,unique=True)
    user_shopp_cart=db.Column(db.Integer)
    user_pur=db.Column(db.Integer)
    
    def __init__(self,username, name, password, email,user_pur,user_shopp_cart):
        self.username =username
        self.password = password
        self.name = name 
        self.email = email
        self.user_shopp_cart = user_shopp_cart
        self.user_pur=user_pur
        
        
    def __repr__(self):
        return "<User %r>" % self.username


class Product(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer,primary_key=True)
    p_name= db.Column(db.String,unique=True)
    main_ing = db.Column(db.String)
    quant_p= db.Column(db.Integer)

    def __init__(self,p_name,main_ing,quant_p):
        p_name = p_name
        main_ing = main_ing
        quant_p = quant_p
        
    def __repr__(self):
        return "<Product %r>" % self.p_name
    
    
    