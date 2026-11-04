<div dir="rtl">

# 🎬 سیستم هوشمند پیشنهاددهنده فیلم و کتاب (Cross-Domain Recommender System)

**تهیه‌کننده و توسعه‌دهنده نرم‌افزار:** ابراهیم یدالهی  
**درس:** آزمایشگاه هوش مصنوعی  
**مخزن گیت‌هاب:** [movie-book-recommender](https://github.com/ebrahimy5280-del/movie-book-recommender)

---

> 💡 **معرفی و چشم‌انداز سامانه:**  
> این پروژه با هدف طراحی، ممیزی و پیاده‌سازی یک **عامل هوشمند پیشنهاددهنده ترکیبی فیلم و کتاب** بر بستر اصول مهندسی نرم‌افزار و یادگیری ماشین توسعه یافته است. مخزن حاضر به شکلی ساختاریافته شامل تکالیف هفتگی کلاسی و فازهای سه‌گانه پروژه اصلی (تعریف مسئله، ممیزی داده و تحلیل اکتشافی) به همراه تمامی کدها، پایپ‌لاین‌ها، اسکریپت‌های تحلیلی و مستندات فنی است.

---

## 🗂️ ساختار جامع مخزن (Repository Architecture)

مخزن گیت‌هاب جهت جداسازی شفاف تکالیف هفتگی آزمایشگاه از روند گام‌به‌گام پروژه پایانی، به ساختار استاندارد زیر سازمان‌دهی شده است:

</div>

```text
movie-book-recommender/
│
├── weekly_assignments/                     # تکالیف و نوت‌بوک‌های هفتگی آزمایشگاه
│   ├── check_env.ipynb                     # بررسی پایداری محیط اجرا و نسخه‌ها
│   ├── lab2_pathfinding.ipynb              # شبیه‌سازی و مقایسه الگوریتم‌های جستجو
│   └── README.md                           # گزارش و زمان‌بندی هفتگی آزمایشگاه
│
├── movie_book_recommender_project/         # بسته اصلی سیستم هوشمند توصیه‌گر
│   ├── Step-1/                             # گام اول: تعریف مسئله و عامل هوشمند
│   │   ├── notes/
│   │   │   └── risks.md                    # مستندات ریسک‌ها و معیارهای ارزیابی
│   │   ├── recommender_agent.py            # پیاده‌سازی شبیه‌سازی عامل‌های هوشمند
│   │   └── README.md                       # مستندات فنی و گزارش فاز اول
│   │
│   ├── Step-2/                             # گام دوم: ممیزی داده و معماری سیستم
│   │   ├── data/
│   │   │   ├── train.csv                   # داده‌های بخش آموزش (۸۰٪)
│   │   │   ├── test.csv                    # داده‌های بخش ارزیابی و آزمون (۲۰٪)
│   │   │   └── rating_evaluation.png       # نمودار بصری ارزیابی تعاملات
│   │   ├── src/
│   │   │   ├── data_loader.py              # خط لوله بارگذاری، پاک‌سازی و تفکیک داده
│   │   │   ├── evaluation.py               # اسکریپت اعتبارسنجی تخلخل و ممیزی نشت داده
│   │   │   └── evaluation.ipynb            # نوت‌بوک تعاملی ماتریس تعاملات
│   │   ├── DESIGN.md                       # سند جامع طراحی معماری سامانه
│   │   ├── documentation.md                # مستندات فنی و جداول ممیزی گام دوم
│   │   └── README.md                       # گزارش تفصیلی پیاده‌سازی گام دوم
│   │
│   ├── Step-3/                             # گام سوم: تحلیل اکتشافی داده‌ها (EDA)
│   │   ├── data/
│   │   │   ├── items.csv                   # متادیتا و خصوصیات اقلام (فیلم و کتاب)
│   │   │   ├── ratings.csv                 # لاگ خام تعاملات و امتیازات کاربران
│   │   │   └── eda_analysis.png            # خروجی گرافیکی ۴ نمودار تحلیلی (DPI 300)
│   │   ├── src/
│   │   │   └── eda.ipynb                   # پایپ‌لاین محاسباتی و بصری‌سازی EDA
│   │   └── README.md                       # گزارش تخصصی پیاده‌سازی کدنویسی گام سوم
│   │
│   ├── environment.yml                     # تنظیمات وابستگی‌های محیط Conda
│   └── requirements.txt                    # فهرست وابستگی‌های پایتونی با pip
│
└── README.md                               # شناسنامه و راهنمای کلان کل مخزن
```

<div dir="rtl">

---

## 📌 وضعیت و پیشرفت فازهای سه‌گانه پروژه

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">فاز پروژه</th>
      <th style="text-align: right;">اهداف کلیدی</th>
      <th style="text-align: right;">ماژول‌ها و فایل‌های تحویلی</th>
      <th style="text-align: right;">وضعیت</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>گام اول (Step-1)</b></td>
      <td style="text-align: right;">فرمولاسیون مسئله در چارچوب PEAS، شبیه‌سازی عامل‌های تصادفی، واکنشی و مدل‌محور</td>
      <td style="text-align: right;" dir="ltr"><code>recommender_agent.py</code>, <code>risks.md</code></td>
      <td style="text-align: right;">✔️ تکمیل و مستندسازی شد[cite: 1]</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>گام دوم (Step-2)</b></td>
      <td style="text-align: right;">آماده‌سازی داده‌ها، جداسازی ۸۰/۲۰، ممیزی عدم نشت داده (Leakage) و طراحی معماری سیستم</td>
      <td style="text-align: right;" dir="ltr"><code>data_loader.py</code>, <code>evaluation.py</code>, <code>DESIGN.md</code></td>
      <td style="text-align: right;">✔️ تکمیل و مستندسازی شد[cite: 1]</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>گام سوم (Step-3)</b></td>
      <td style="text-align: right;">ممیزی کیفیت، آمار توصیفی برداری، مقایسه میان‌حوزه‌ای و رسم ۴ نمودار تحلیلی Matplotlib</td>
      <td style="text-align: right;" dir="ltr"><code>eda.ipynb</code>, <code>eda_analysis.png</code>, <code>README.md</code></td>
      <td style="text-align: right;">✔️ تکمیل و مستندسازی شد[cite: 1, 11]</td>
    </tr>
  </tbody>
</table>

---

## 🧩 فاز اول: تعریف مسئله و شبیه‌سازی عامل‌های هوشمند (Step-1)

در این گام، سامانه پیشنهاددهنده در قالب مسئله عامل هوشمند با مشخصه‌های محیطی گسسته، مشاهده‌پذیری جزئی و پویا مدل‌سازی شد[cite: 1]:

* **عامل تصادفی (Random Agent):** انتخاب بدون دانش پیشین به عنوان خط مبنای مقایسه.
* **عامل واکنشی (Reflex Agent):** تصمیم‌گیری مستقیم بر اساس آخرین ترجیح و بازخورد ثبت‌شده کاربر.
* **عامل مبتنی بر مدل (Model-Based Agent):** ذخیره‌سازی تاریخچه تعاملات و امتیازها جهت یادگیری تدریجی سلایق کاربر در طول زمان.

---

## 📊 فاز دوم: مدیریت داده‌ها، ممیزی و ارزیابی آفلاین (Step-2)

در گام دوم، تمرکز بر تبدیل شبیه‌سازی به یک پایپ‌لاین استاندارد داده‌محور بود:
1. **جداسازی Train/Test:** تقسیم قطعی داده‌ها با نسبت ۸۰ به ۲۰ برای جلوگیری از بیش‌برازش.
2. **بررسی عدم نشت اطلاعات (Data Leakage):** تضمین صفر بودن اشتراک زوج‌های (کاربر-آیتم) میان مجموعه‌های آموزش و آزمون توسط اسکریپت `evaluation.py`.
3. **تحلیل تنکی ماتریس (Sparsity Rate):** اندازه‌گیری میزان خانه‌های تهی ماتریس تعاملات جهت ارزیابی آمادگی الگوریتم در مواجهه با شروع سرد (Cold Start).
4. **سند جامع طراحی معماری (`DESIGN.md`):** تدوین ساختار ریاضی معیارهای رتبه‌بندی Precision@K، Recall@K و فرمولاسیون فیلترینگ مشارکتی.

---

## 📈 فاز سوم: تحلیل اکتشافی داده‌ها (EDA) و بصری‌سازی (Step-3)

در گام سوم، کلیه آزمون‌های سلامت داده و آماره‌های توصیفی به همراه گرید گرافیکی چهارگانه در نوت‌بوک `eda.ipynb` کدنویسی و اجرا شد[cite: 1, 11]:

<div align="center">

![نمودارهای تحلیل اکتشافی داده‌ها](movie_book_recommender_project/Step-3/data/eda_analysis.png)

</div>

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">نمودار تحلیلی</th>
      <th style="text-align: right;">نوع بصری‌سازی</th>
      <th style="text-align: right;">خروجی شاخص</th>
      <th style="text-align: right;">نتیجه تحلیلی برای مدل توصیه‌گر</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>توزیع نمرات (Rating Distribution)</b></td>
      <td style="text-align: right;">Bar / Histogram</td>
      <td style="text-align: right;">۷۰.۸٪ نمرات در بازه ۴ و ۵[cite: 11]</td>
      <td style="text-align: right;">وجود سوگیری مثبت (Positivity Bias)؛ لزوم نرمال‌سازی انحراف از میانگین (Mean-Centering)</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>حجم تعاملات رسانه‌ها (Volume by Type)</b></td>
      <td style="text-align: right;">Categorical Bar</td>
      <td style="text-align: right;">۱۳ فیلم و ۱۱ کتاب[cite: 11]</td>
      <td style="text-align: right;">توازن کامل تعاملات؛ مدل نهایی دچار غلبه یا عدم تقارن کلاس نخواهد شد[cite: 11]</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>نمودار جعبه‌ای نمرات (Boxplot)</b></td>
      <td style="text-align: right;">Box & Whisker</td>
      <td style="text-align: right;">میانه یکسان ۴.۰ و نبود Outlier[cite: 11]</td>
      <td style="text-align: right;">همگنی رفتار امتیازدهی؛ امکان به‌کارگیری ساختار پیشنهاددهنده مشترک (Cross-Domain)[cite: 11]</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>پراکندگی تعامل کاربران (User Engagement)</b></td>
      <td style="text-align: right;">Discrete Histogram</td>
      <td style="text-align: right;">۴ تعامل به ازای هر کاربر[cite: 11]</td>
      <td style="text-align: right;">تعادل داده‌های اولیه؛ ارزیابی عادلانه عملکرد فیلترینگ مشارکتی بر پایه کاربر[cite: 11]</td>
    </tr>
  </tbody>
</table>

---

## 🛠️ مشخصات فنی و محیط اجرایی سیستم

پایپ‌لاین‌ها بر روی سیستم‌عامل ویندوز ۱۱ ویرایش ۶۴ بیتی پیاده‌سازی و تست شده‌اند:

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">ابزار / کتابخانه</th>
      <th style="text-align: right;">نسخه ثبت‌شده</th>
      <th style="text-align: right;">نقش در پایپ‌لاین نرم‌افزار</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>Python</b></td>
      <td style="text-align: right;" dir="ltr">3.14.0</td>
      <td style="text-align: right;">محیط اجرای اصلی اسکریپت‌ها</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>Pandas</b></td>
      <td style="text-align: right;" dir="ltr">3.0.5</td>
      <td style="text-align: right;">دستکاری دیتافریم‌ها، ممیزی کیفیت و محاسبات تجمیعی</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>NumPy</b></td>
      <td style="text-align: right;" dir="ltr">2.5.2</td>
      <td style="text-align: right;">عملیات برداری ریاضی و استخراج آماره‌های عددی</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>Matplotlib</b></td>
      <td style="text-align: right;" dir="ltr">3.11.1</td>
      <td style="text-align: right;">موتور رسم گرید ۴ نمودار تحلیلی با تنظیم مستقیم تیک‌های محوری</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>Jupyter Lab / Notebook</b></td>
      <td style="text-align: right;" dir="ltr">1.1.1</td>
      <td style="text-align: right;">محیط توسعه نوت‌بوک‌های تعاملی محاسباتی</td>
    </tr>
  </tbody>
</table>

---

## 🚀 راهنمای نصب و راه‌اندازی سریع (Quick Start)

جهت کلون کردن مخزن و راه‌اندازی کامل محیط اجرایی:

### ۱. دریافت مخزن
```bash
git clone [https://github.com/ebrahimy5280-del/movie-book-recommender.git](https://github.com/ebrahimy5280-del/movie-book-recommender.git)
cd movie-book-recommender
```

### ۲. فعال‌سازی محیط مجازی Conda
```bash
conda env create -f movie_book_recommender_project/environment.yml
conda activate ailab
```
*یا با استفاده از Pip:*
```bash
python -m pip install -r movie_book_recommender_project/requirements.txt
```

### ۳. اجرای کدهای پروژه
```bash
# اجرای شبیه‌سازی عامل‌های گام اول
python movie_book_recommender_project/Step-1/recommender_agent.py

# اجرای ممیزی و ارزیابی نشت داده گام دوم
python movie_book_recommender_project/Step-2/src/evaluation.py

# اجرای محیط نوت‌بوک تحلیلی گام سوم
cd movie_book_recommender_project/Step-3/src
jupyter notebook eda.ipynb
```

---

## 🗺️ برنامه و نقشه راه ادامه توسعه (Roadmap)

- [x] پیاده‌سازی و شبیه‌سازی عامل‌های سه‌گانه هوشمند (گام اول)[cite: 1]
- [x] طراحی ماتریس ارزیابی و سند طراحی معماری سامانه (گام دوم)[cite: 1]
- [x] توسعه خط لوله ارزیابی عدم نشت داده و نرخ تخلخل (گام دوم)[cite: 1]
- [x] اجرای پایپ‌لاین تحلیل اکتشافی داده‌ها (EDA) و حل تعارضات کتابخانه ترسیم (گام سوم)[cite: 1, 6]
- [x] مستندسازی اختصاصی نقش پیاده‌سازی و کدنویسی برای گام‌های اول، دوم و سوم[cite: 1]
- [ ] پیاده‌سازی مدل‌های مشارکتی (Collaborative Filtering) بر پایه ماتریس همسایگی
- [ ] پیاده‌سازی الگوریتم رتبه‌بندی مجدد تنوع‌محور (Maximal Marginal Relevance - MMR)
- [ ] ارزیابی برخط سامانه با سناریوهای شروع سرد (Cold Start) کاربران جدید

---

## 👤 درباره توسعه‌دهنده

* **توسعه‌دهنده:** ابراهیم یدالهی
* **دانشگاه:** شهید باهنر کرمان
* **گیت‌هاب:** [@ebrahimy5280-del](https://github.com/ebrahimy5280-del)
* **پروژه:** سامانه هوشمند پیشنهاددهنده فیلم و کتاب (`movie-book-recommender`)

</div>
