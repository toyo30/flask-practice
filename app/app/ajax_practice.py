from app import app

from flask import request, render_template, jsonify



@app.route('/ajaxTest', methods=['GET'])
def testIndex():
    return render_template("ajax/ajax_practice3.html")


@app.route('/ajaxTest_practice', methods=['GET'])
def testAjax():
    request_args = request.args.to_dict()
    print(request_args)
    return render_template('ajax/ajax_practice3.html')


@app.route('/ajaxTest', methods=['POST'])
def testAjax_done():
    print(request.form.to_dict())
    ajax = request.form.get("ajaxText3")
    print(ajax)
    #request_args2 = request.args.to_dict('ajax_text')
    # print(request_args2)
    return jsonify({"status" : 1})

# @app.route('/ajax', methods=['GET'])
# def index():

#     return render_template('ajax_practice3.html')

# @app.route('/ajax_p',methods=['GET'])
# def ajax_practice():
#     request_args = request.args.to_dict()

#     print(request_args)


#     # return render_template('ajax_practice.html')
#     return render_template('ajax-practice/ajax_practice3.html')




# @app.route('/ajax_p', methods=['POST'])
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
#     return render_template('ajax-practice/ajax_practice2.html')






