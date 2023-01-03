from flask import Flask, render_template, request
import random
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    mylist = []
    roles = []
    numbers = []
    last_move_cards = []
    last_move_numbers = []
    if request.method == 'POST':
        if request.form.get('scenario') == 'takavar':
            if request.form.get('action10') == '10 نفره':
                mylist = ['کارآگاه', 'دکتر', 'نگهبان', 'تفنگدار', 'تکاور', 'شهروند ساده', 'شهروند ساده', 'گادفادر', 'ناتو', 'گروگانگیر']
                numbers = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ']
            elif request.form.get('action11') == '11 نفره':
                mylist = ['کارآگاه', 'دکتر', 'نگهبان', 'تفنگدار', 'تکاور', 'شهروند ساده', 'شهروند ساده', 'گادفادر', 'ناتو', 'گروگانگیر', 'شهروند ساده']
                numbers = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ', '11. ']
            elif request.form.get('action12') == '12 نفره':
                mylist = ['کارآگاه', 'دکتر', 'نگهبان', 'تفنگدار', 'تکاور', 'شهروند ساده', 'شهروند ساده', 'گادفادر', 'ناتو', 'گروگانگیر', 'شهروند ساده', 'مافیا ساده']
                numbers = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ', '11. ', '12. ']
            elif request.form.get('action13') == '13 نفره':
                mylist = ['کارآگاه', 'دکتر', 'نگهبان', 'تفنگدار', 'تکاور', 'شهروند ساده', 'شهروند ساده', 'گادفادر', 'ناتو', 'گروگانگیر', 'شهروند ساده', 'مافیا ساده', 'شهروند ساده']
                numbers = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ', '11. ', '12. ', '13. ']
            elif request.form.get('action14') == '14 نفره':
                mylist = ['کارآگاه', 'دکتر', 'نگهبان', 'تفنگدار', 'تکاور', 'شهروند ساده', 'شهروند ساده', 'گادفادر', 'ناتو', 'گروگانگیر', 'شهروند ساده', 'مافیا ساده', 'شهروند ساده', 'مافیا ساده']
                numbers = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ', '11. ', '12. ', '13. ', '14. ']
            elif request.form.get('action15') == '15 نفره':
                mylist = ['کارآگاه', 'دکتر', 'نگهبان', 'تفنگدار', 'تکاور', 'شهروند ساده', 'شهروند ساده', 'گادفادر', 'ناتو', 'گروگانگیر', 'شهروند ساده', 'مافیا ساده', 'شهروند ساده', 'مافیا ساده', 'شهروند ساده']
                numbers = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ', '11. ', '12. ', '13. ', '14. ', '15. ']
            else:
                mylist = []
        elif request.form.get('scenario') == 'godfather':
            last_move_cards = ['سکوت بره ها', 'افشای هویت', 'ذهن زیبا', 'دستبند', 'تغییر چهره']
            last_move_numbers = ['1. ', '2. ', '3. ', '4. ', '5. ']
            if request.form.get('action10') == '10 نفره':
                mylist = ['کنستانتین', 'دکتر واتسون', 'همشهری کین', 'لئون حرفه ای', 'شهروند ساده', 'شهروند ساده', 'گادفادر', 'ساول گودمن', 'ماتادور', 'نوستراداموس']
                numbers = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ']
            elif request.form.get('action11') == '11 نفره':
                mylist = ['کنستانتین', 'دکتر واتسون', 'همشهری کین', 'لئون حرفه ای', 'شهروند ساده', 'شهروند ساده', 'گادفادر', 'ساول گودمن', 'ماتادور', 'نوستراداموس', 'شهروند ساده']
                numbers = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ', '11. ']
            elif request.form.get('action12') == '12 نفره':
                mylist = ['کنستانتین', 'دکتر واتسون', 'همشهری کین', 'لئون حرفه ای', 'شهروند ساده', 'شهروند ساده', 'گادفادر', 'ساول گودمن', 'ماتادور', 'نوستراداموس', 'شهروند ساده', 'مافیا ساده']
                numbers = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ', '11. ', '12. ']
            elif request.form.get('action13') == '13 نفره':
                mylist = ['کنستانتین', 'دکتر واتسون', 'همشهری کین', 'لئون حرفه ای', 'شهروند ساده', 'شهروند ساده', 'گادفادر', 'ساول گودمن', 'ماتادور', 'نوستراداموس', 'شهروند ساده', 'مافیا ساده', 'شهروند ساده']
                numbers = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ', '11. ', '12. ', '13. ']
            elif request.form.get('action14') == '14 نفره':
                mylist = ['کنستانتین', 'دکتر واتسون', 'همشهری کین', 'لئون حرفه ای', 'شهروند ساده', 'شهروند ساده', 'گادفادر', 'ساول گودمن', 'ماتادور', 'نوستراداموس', 'شهروند ساده', 'مافیا ساده', 'شهروند ساده', 'مافیا ساده']
                numbers = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ', '11. ', '12. ', '13. ', '14. ']
            elif request.form.get('action15') == '15 نفره':
                mylist = ['کنستانتین', 'دکتر واتسون', 'همشهری کین', 'لئون حرفه ای', 'شهروند ساده', 'شهروند ساده', 'گادفادر', 'ساول گودمن', 'ماتادور', 'نوستراداموس', 'شهروند ساده', 'مافیا ساده', 'شهروند ساده', 'مافیا ساده', 'شهروند ساده']
                numbers = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ', '11. ', '12. ', '13. ', '14. ', '15. ']
            else:
                mylist = []
        else:
            mylist=["لطفا سناریو را انتخاب کنید"]
        
    elif request.method == 'GET':
        return render_template('index.html', roles=roles)
    
    random.shuffle(mylist)
    random.shuffle(last_move_cards)
    
    mylist = [n+m for m,n in zip(mylist, numbers)]
    last_move_cards = [n+m for m,n in zip(last_move_cards, last_move_numbers)]
    
    roles = json.dumps(mylist, ensure_ascii=False)
    cards = json.dumps(last_move_cards, ensure_ascii=False)
    
    return render_template('index.html', roles=roles, cards=cards)
    
if __name__ == '__main__':
    app.run(threaded=True)
