from flask import request, jsonify, make_response,render_template
from app.models import  PostgresModel,MySQLModel
from app import app, db



# Fetching data From MySQL
@app.route("/MySQL", methods=['GET', 'POST'])
def home():
    x = MySQLModel.query.all()
    print(type(x))
    print(x[0].id)
    data = []
    for i in x:
        data1 = []
        print(i.id,i.first_name,i.last_name)
        data1.append(i.id)
        data1.append(i.first_name)
        data1.append(i.last_name)
        data.append(data1)

    return render_template("index.html",data = data)
    
    # return make_response(jsonify({"mysql":data}))


# Fetching data From PostgreSQL
@app.route("/PostgreSQL", methods=['GET', 'POST'])
def Postgresql():
   
    x = PostgresModel.query.all()
    print(x)
    data = []
    for i in x:
        data1 = []
        print(i.id,i.first_name,i.last_name)
        data1.append(i.id)
        data1.append(i.first_name)
        data1.append(i.last_name)
        data.append(data1)

    return render_template("index.html",data = data)
    # data = {}
    # for i in x:
        
    #     data1 = {
    #         "id":i.id,
    #         "first_name":i.first_name
    #     }
    #     data["user"+str(i.id)] = data1
        
   
    # return make_response(jsonify(data), 200)


# @app.route("/Postgreadd", methods=['GET', 'POST'])
# def Postgres():
#     x= PostgresModel(id = 9,first_name = "Shubhangi",last_name = "chaubey",email = "chat@gmail.com",password = "123")
#     db.session.add(x)
#     db.session.commit()
#     return make_response("ok", 200)




# @app.route("/madd", methods=['GET', 'POST'])
# def MySQLadd():
#     x = MySQLModel(id = 1,first_name = "MySQl_Shubhangi",last_name = "chaturvedi",email = "chat@gmail.com",password = "123")
#     db.session.add(x)
#     db.session.commit()
#     return make_response("ok", 200)


