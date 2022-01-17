# from flask import Flask, request, jsonify, render_template
# from pymysql_practice_33 import db_nameinsert

# app=Flask(__name__)


# @app.route('/ajaxTest', methods=['GET'])
# def index():

#     return render_template('ajax_practice2.html')

# @app.route('/ajax_practice2',methods=['GET'])
# def ajax_practice():
#     request_args = request.args.to_dict()

#     print(request_args)


#     # return render_template('ajax_practice.html')
#     return render_template('ajax_practice2.html')




# @app.route('/ajax_practice2',methods=['POST'])
# def ajax_practice_done():

#     #html에서 데이터를 못주고받는상태인거같음음
#    #requestparam이 없어서 일단 이렇게했는데 맞는지? ㅇㅇ 맞아요

#     #request_args2 = request.form.get('ajax_text2')
#     request_args2 = request.form.get('ajax_text2')
#                             #post방식일때 request.form.get(ajax의 data 키값)
#                             #get방식일때 request.args.get(ajax의 data 키값)
#     print(request_args2)

#     # db_nameinsert(request_args2)



#     #return render_template('ajax_practice.html')
#     return render_template('ajax_practice2.html')






# if __name__=='__main__':
#     app.run(port=5002)