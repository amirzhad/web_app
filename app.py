from flask import Flask, render_template, request
import random
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action10') == '10 نفره':
            mylist = ["کارآگاه", "دکتر", "نگهبان", "تفنگدار", "تکاور", "شهروند ساده", "شهروند ساده", "گادفادر", "ناتو", "گروگانگیر"]
            random.shuffle(mylist)
            encodedUnicode = json.dumps(mylist, ensure_ascii=False)
            return encodedUnicode
        elif request.form.get('action11') == '11 نفره':
            mylist = ["کارآگاه", "دکتر", "نگهبان", "تفنگدار", "تکاور", "شهروند ساده", "شهروند ساده", "گادفادر", "ناتو", "گروگانگیر", "شهروند ساده"]
            random.shuffle(mylist)
            encodedUnicode = json.dumps(mylist, ensure_ascii=False)
            return encodedUnicode
        elif request.form.get('action12') == '12 نفره':
            mylist = ["کارآگاه", "دکتر", "نگهبان", "تفنگدار", "تکاور", "شهروند ساده", "شهروند ساده", "گادفادر", "ناتو", "گروگانگیر", "شهروند ساده", "مافیا ساده"]
            random.shuffle(mylist)
            encodedUnicode = json.dumps(mylist, ensure_ascii=False)
            return encodedUnicode
        elif request.form.get('action13') == '13 نفره':
            mylist = ["کارآگاه", "دکتر", "نگهبان", "تفنگدار", "تکاور", "شهروند ساده", "شهروند ساده", "گادفادر", "ناتو", "گروگانگیر", "شهروند ساده", "مافیا ساده", "شهروند ساده"]
            random.shuffle(mylist)
            encodedUnicode = json.dumps(mylist, ensure_ascii=False)
            return encodedUnicode
        elif request.form.get('action14') == '14 نفره':
            mylist = ["کارآگاه", "دکتر", "نگهبان", "تفنگدار", "تکاور", "شهروند ساده", "شهروند ساده", "گادفادر", "ناتو", "گروگانگیر", "شهروند ساده", "مافیا ساده", "شهروند ساده", "مافیا ساده"]
            random.shuffle(mylist)
            encodedUnicode = json.dumps(mylist, ensure_ascii=False)
            return encodedUnicode
        elif request.form.get('action15') == '15 نفره':
            mylist = ["کارآگاه", "دکتر", "نگهبان", "تفنگدار", "تکاور", "شهروند ساده", "شهروند ساده", "گادفادر", "ناتو", "گروگانگیر", "شهروند ساده", "مافیا ساده", "شهروند ساده", "مافیا ساده", "شهروند ساده"]
            random.shuffle(mylist)
            encodedUnicode = json.dumps(mylist, ensure_ascii=False)
            return encodedUnicode
        else:
            mylist = []
    
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run(threaded=True)
