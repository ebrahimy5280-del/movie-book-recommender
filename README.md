<div dir="rtl" align="right">

# 🎬 سامانه هوشمند و چندحوزه‌ای پیشنهاددهنده فیلم و کتاب
# (Cross-Domain Recommender System)

**تهیه‌کننده: ابراهیم یدالهی**  
**درس:** آزمایشگاه هوش مصنوعی  
**مخزن اصلی گیت‌هاب:** [movie-book-recommender](https://github.com/ebrahimy5280-del/movie-book-recommender)

---

> 💡 **چکیده اجرایی و معماری کلان پروژه:**  
> سامانه حاضر یک سیستم پیشنهاددهنده هوشمند چندحوزه‌ای (Cross-Domain Recommender System) است که با هدف مدل‌سازی، پیش‌بینی و پالایش علایق کاربران در دو رسانه مکمل فیلم و کتاب بر مبنای اصول مهندسی نرم‌افزار، چارچوب‌های عامل هوشمند و یادگیری ماشین طراحی و توسعه داده شده است. ساختار این مخزن به‌گونه‌ای طراحی شده که تفکیک کاملی میان تکالیف هفتگی آزمایشگاه و فازهای تخصصی توسعه سامانه برقرار سازد و تمامی مراحل از مدل‌سازی تئوری در قالب چارچوب‌های عامل‌ها تا ممیزی کیفیت داده، مهندسی ویژگی‌ها و معماری مدل‌های پایه را با رعایت استانداردهای آکادمیک و فنی ارائه دهد.

---

## 🗂️ معماری و ساختار جامع فایل‌ها و دایرکتوری‌ها

ساختار مخزن بر مبنای تفکیک ماژولار و سازمان‌دهی ایزوله کدهای پژوهشی در کنار تکالیف کارگاهی شکل گرفته است:

```text
movie-book-recommender/
│
├── weekly_assignments/                     # تکالیف و نوت‌بوک‌های هفتگی آزمایشگاه هوش مصنوعی
│   ├── check_env.ipynb                     # جلسه ۱: بررسی پایداری وابستگی‌های محیط، پکیج‌ها و سخت‌افزار
│   ├── lab2_pathfinding.ipynb              # جلسات ۲ و ۳: مقایسه الگوریتم‌های جستجوی ناآگاهانه و آگاهانه (BFS, DFS, A*)
│   ├── lab3_nim_minimax_eda_graphical.ipynb# جلسه ۴: بازی نیم با Minimax، هرس آلفا-بتا، EDA و چالش معکوس Misère
│   ├── lab4_nim_ml_sklearn.ipynb           # جلسه ۵: یادگیری نظارت‌شده، تله دقت، مهندسی ویژگی nim_sum و F1
│   ├── tree_depth_curve.png                # نمودار استخراج‌شده تحلیل بیش‌برازش عمق درخت تصمیم (max_depth)
│   └── README.md                           # گزارش جامع، جداول مقایسه‌ای و تحلیل مشاهده-دلیل-نتیجه تکالیف ۱ تا ۵
│
├── movie_book_recommender_project/         # بسته اصلی توسعه سیستم هوشمند پیشنهاددهنده
│   ├── Step-1/                             # گام اول: تعریف مسئله، مدل‌سازی محیط و شبیه‌سازی عامل‌ها
│   │   ├── notes/
│   │   │   └── risks.md                    # مستندات تحلیلی ریسک‌ها، سوگیری‌ها و معیارهای ارزیابی آفلاین
│   │   ├── recommender_agent.py            # پیاده‌سازی شیءگرای شبیه‌سازی عامل‌های تصادفی، واکنشی و مدل‌محور
│   │   └── README.md                       # مستندات و گزارش جامع تحلیلی فاز اول
│   │
│   ├── Step-2/                             # گام دوم: مهندسی داده، ممیزی، معماری سیستم و تفکیک پایپ‌لاین
│   │   ├── data/
│   │   │   ├── train.csv                   # پایگاه داده آموزش با نسبت ۸۰٪
│   │   │   ├── test.csv                    # پایگاه داده آزمون با نسبت ۲۰٪ (تفکیک قطعی)
│   │   │   └── rating_evaluation.png       # مصورسازی ارزیابی توزیع بازخوردها و پوشش داده‌ها
│   │   ├── src/
│   │   │   ├── data_loader.py              # خط لوله بارگذاری خودکار، پاک‌سازی و تفکیک بدون نشت داده
│   │   │   ├── evaluation.py               # موتور محاسباتی ممیزی نشت داده، نرخ تخلخل و شاخص‌های آماری
│   │   │   └── evaluation.ipynb            # نوت‌بوک تعاملی تحلیل ماتریس تعاملات و نمایش ساختار رابطه‌ای
│   │   ├── DESIGN.md                       # سند جامع معماری، روابط ریاضی، طرح‌واره داده‌ها و استراتژی ارزیابی
│   │   ├── documentation.md                # گزارش مستندسازی فنی و ممیزی‌های انجام‌شده
│   │   └── README.md                       # مستندات تفصیلی و تشریح پایپ‌لاین گام دوم
│   │
│   ├── Step-3/                             # گام سوم: تحلیل اکتشافی جامع داده‌ها (EDA) و مصورسازی آماری
│   │   ├── data/
│   │   │   ├── items.csv                   # جدول ویژگی‌ها و متادیتای اقلام (فیلم‌ها و کتاب‌ها)
│   │   │   ├── ratings.csv                 # ماتریس خام تعاملات، شناسه کاربران، امتیازها و برچسب‌های زمانی
│   │   │   └── eda_analysis.png            # خروجی گرافیکی گرید ۴ نمودار تحلیلی با کیفیت بالا (DPI 300)
│   │   ├── src/
│   │   │   └── eda.ipynb                   # نوت‌بوک محاسباتی و تحلیلی EDA با پیاده‌سازی ممیزی برداری
│   │   └── README.md                       # مستندات فنی و گزارش جامع پیاده‌سازی گام سوم
│   │
│   ├── Step-4/                             # گام چهارم: مهندسی مدل‌های پایه (Baselines) و پروتکل اعتبارسنجی
│   │   ├── DESIGN.md                       # سند معماری، فرمولاسیون ریاضی مدل‌های پایه، منظم‌سازی و متریک‌ها
│   │   └── README.md                       # گزارش تحلیلی نقش طراح سیستم و مهار تله دقت در سیستم‌های پیشنهاددهنده
│   │
│   ├── environment.yml                     # تعریف مشخصات و وابستگی‌های محیط ایزوله Conda
│   └── requirements.txt                    # فهرست دقیق پکیج‌های پایتون جهت نصب با pip
│
└── README.md                               # راهنما، شناسنامه و داشبورد مدیریتی کلان کل مخزن
```

---

## 📊 داشبورد وضعیت و ماتریس پیشرفت فازهای چهارگانه پروژه

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">فاز و گام پروژه</th>
      <th style="text-align: right;">اهداف کلیدی و استانداردهای مهندسی</th>
      <th style="text-align: right;">ماژول‌ها و پیوندهای مخزن</th>
      <th style="text-align: right;">وضعیت</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>گام اول (Step-1)</b></td>
      <td style="text-align: right;">فرمولاسیون مسئله در چارچوب PEAS، بررسی مشخصه‌های محیطی، پیاده‌سازی عامل‌های تصادفی، واکنشی و مبتنی بر مدل</td>
      <td style="text-align: right;" dir="ltr"><a href="movie_book_recommender_project/Step-1/recommender_agent.py"><code>recommender_agent.py</code></a>, <a href="movie_book_recommender_project/Step-1/notes/risks.md"><code>risks.md</code></a></td>
      <td style="text-align: right;">✔️ تکمیل و مستندسازی شد</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>گام دوم (Step-2)</b></td>
      <td style="text-align: right;">جمع‌آوری داده‌ها، جداسازی قطعی ۸۰/۲۰، سنجش نرخ تخلخل (Sparsity)، اثبات ریاضی عدم نشت داده (Data Leakage) و تدوین سند طراحی معماری</td>
      <td style="text-align: right;" dir="ltr"><a href="movie_book_recommender_project/Step-2/src/data_loader.py"><code>data_loader.py</code></a>, <a href="movie_book_recommender_project/Step-2/src/evaluation.py"><code>evaluation.py</code></a>, <a href="movie_book_recommender_project/Step-2/DESIGN.md"><code>DESIGN.md</code></a></td>
      <td style="text-align: right;">✔️ تکمیل و مستندسازی شد</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>گام سوم (Step-3)</b></td>
      <td style="text-align: right;">ممیزی کیفیت داده‌ها، استخراج آماره‌های توصیفی برداری، مقایسه رفتار رسانه‌ها و تولید بوم گرافیکی ۴ نمودار تحلیلی با کیفیت ۳۰۰ DPI</td>
      <td style="text-align: right;" dir="ltr"><a href="movie_book_recommender_project/Step-3/src/eda.ipynb"><code>eda.ipynb</code></a>, <a href="movie_book_recommender_project/Step-3/data/eda_analysis.png"><code>eda_analysis.png</code></a>, <a href="movie_book_recommender_project/Step-3/README.md"><code>README.md</code></a></td>
      <td style="text-align: right;">✔️ تکمیل و مستندسازی شد</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>گام چهارم (Step-4)</b></td>
      <td style="text-align: right;">مهار تله دقت، فرمولاسیون ریاضی مدل‌های پایه (Global Mean، Biases و Popularity)، گزینش معیارهای ارزیابی (RMSE, MAE, Recall@K, NDCG@K) و تدوین سند معماری</td>
      <td style="text-align: right;" dir="ltr"><a href="movie_book_recommender_project/Step-4/DESIGN.md"><code>DESIGN.md</code></a>, <a href="movie_book_recommender_project/Step-4/README.md"><code>README.md</code></a></td>
      <td style="text-align: right;">✔️ تکمیل و مستندسازی شد</td>
    </tr>
  </tbody>
</table>

---

## 🧩 فاز اول: فرمولاسیون مسئله، تحلیل محیط و شبیه‌سازی عامل‌های هوشمند (Step-1)

در گام نخست، سیستم پیشنهاددهنده به عنوان یک عامل هوشمند در تعامل با کاربر و محیط محتوا فرمول‌بندی شد:

### ۱. تحلیل چارچوب PEAS
- **معیار عملکرد (Performance Measure):** بیشینه‌سازی تناسب پیشنهادها با سلایق واقعی، افزایش نرخ تبدیل و نرخ رضایت (امتیازهای ۴ و ۵) و کمینه‌سازی خطای پیش‌بینی.
- **محیط (Environment):** اقلام چندحوزه‌ای (فیلم‌ها و کتاب‌ها)، ماتریس تنک تعاملات، ژانرها و ویژگی‌های محتوایی.
- **عملگرها (Actuators):** انتخاب و رتبه‌بندی فهرست پیشنهادی K تایی (Top-K Recommendations) و نمایش به کاربر.
- **حسگرها (Sensors):** لاگ بازخوردهای صریح (امتیازهای عددی ۱ تا ۵) و تاریخچه تعاملات قبلی.

### ۲. ویژگی‌های محیط عامل
محیط پیشنهاددهی بر اساس تعاریف هوش مصنوعی دارای ویژگی‌های زیر است:
- **مشاهده‌پذیری جزئی (Partially Observable):** علایق و انگیزه‌های روانی کاربر به صورت کامل و شفاف در دسترس نیست.
- **غیرقطعی و تصادفی (Stochastic):** واکنش کاربر به یک اثر می‌تواند تحت تأثیر متغیرهای پنهان (خلق‌وخو، زمان تماشا و...) تغییر کند.
- **ترتیبی (Sequential):** هر انتخاب و بازخورد کاربر، وضعیت فضای علایق او را برای پیشنهادهای بعدی دستخوش تغییر می‌کند.
- **پویا (Dynamic):** محتوای کاتالوگ و سلیقه کاربران با گذر زمان تغییر می‌یابد.
- **تک‌عاملی (Single-Agent):** سامانه پیشنهاددهنده به عنوان هسته متمرکز تصمیم‌گیری عمل می‌کند.

### ۳. عامل‌های توسعه‌داده‌شده در [`recommender_agent.py`](movie_book_recommender_project/Step-1/recommender_agent.py)
- 🔹 **عامل تصادفی (Random Agent):** بدون توجه به سوابق و صرفاً بر اساس توزیع یکنواخت تصمیم می‌گیرد؛ این عامل مبنای پایه (Baseline) برای سنجش ارزش افزوده مدل‌های دیگر است.
- 🔹 **عامل واکنشی (Reflex Agent):** تصمیم‌گیری مستقیم بر اساس نگاشت وضعیت به عمل (شرط-عمل)؛ مانند ترجیح ژانر آخرین اثر دیده‌شده.
- 🔹 **عامل مبتنی بر مدل (Model-Based Agent):** نگهداری یک حالت درونی (Internal State) از وزن‌های علایق کاربر به تفکیک ژانرها و به‌روزرسانی تدریجی ماتریس سلایق با دریافت هر فیدبک جدید.

---

## 📊 فاز دوم: خط لوله داده‌ها، ممیزی، معماری سامانه و ارزیابی آفلاین (Step-2)

گام دوم زیرساخت فنی داده‌محور پروژه را پیاده‌سازی کرد:

### ۱. ماژول خط لوله داده‌ها ([`data_loader.py`](movie_book_recommender_project/Step-2/src/data_loader.py))
این اسکریپت وظیفه دریافت، پاک‌سازی، یکسان‌سازی تایپ‌ها و تقسیم قطعی داده‌ها به نسبت ۸۰٪ آموزش ([`train.csv`](movie_book_recommender_project/Step-2/data/train.csv)) و ۲۰٪ آزمون ([`test.csv`](movie_book_recommender_project/Step-2/data/test.csv)) را بدون هم‌پوشانی بر عهده دارد.

### ۲. موتور ممیزی و ارزیابی ([`evaluation.py`](movie_book_recommender_project/Step-2/src/evaluation.py))
- **ممیزی نشت داده (Data Leakage Verification):** تضمین صفر بودن اشتراک زوج‌های `(user_id, item_id)` میان مجموعه‌های Train و Test.
- **محاسبه نرخ تخلخل ماتریس (Sparsity Rate):** سنجش میزان تنکی داده‌ها بر اساس فرمول:
  $$\text{Sparsity} = 1 - \frac{\vert{}R\vert{}}{\vert{}U\vert{} \times \vert{}I\vert{}}$$
- **تحلیل ماتریس تعاملات:** مصورسازی وضعیت حضور نمرات در فضای دوبعدی کاربر-آیتم در نوت‌بوک [`evaluation.ipynb`](movie_book_recommender_project/Step-2/src/evaluation.ipynb).

### ۳. سند جامع طراحی معماری سامانه ([`DESIGN.md`](movie_book_recommender_project/Step-2/DESIGN.md))
تدوین روابط ریاضی معیارهای رتبه‌بندی نظیر Precision@K، Recall@K، NDCG@K، فرمولاسیون فیلترینگ مشارکتی بر پایه شباهت کسینوسی و همبستگی پیرسون و راهکارهای مدیریت چالش شروع سرد (Cold Start).

---

## 📈 فاز سوم: تحلیل اکتشافی جامع داده‌ها (EDA) و مصورسازی آماری (Step-3)

در گام سوم، کلیه آزمون‌های سلامت داده و آماره‌های توصیفی به همراه گرید گرافیکی چهارگانه در نوت‌بوک [`eda.ipynb`](movie_book_recommender_project/Step-3/src/eda.ipynb) پیاده‌سازی و اجرا گردید:

<div align="center">

![چهار نمودار اصلی تحلیل اکتشافی داده‌ها](movie_book_recommender_project/Step-3/data/eda_analysis.png)

</div>

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">ردیف</th>
      <th style="text-align: right;">نمودار تحلیلی</th>
      <th style="text-align: right;">نوع بصری‌سازی</th>
      <th style="text-align: right;">خروجی شاخص عددی</th>
      <th style="text-align: right;">تفسیر فنی و نتیجه مهندسی در سیستم پیشنهاددهنده</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>۱</b></td>
      <td style="text-align: right;"><b>توزیع نمرات (Rating Distribution)</b></td>
      <td style="text-align: right;">Bar Plot / Histogram</td>
      <td style="text-align: right;">۷۰.۸٪ نمرات در بازه ۴ و ۵</td>
      <td style="text-align: right;">وجود چولگی به راست و سوگیری مثبت (Positivity Bias)؛ نشان‌دهنده لزوم اجرای نرمال‌سازی انحراف از میانگین (Mean-Centering) در گام مدل‌سازی مشارکتی.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>۲</b></td>
      <td style="text-align: right;"><b>حجم تعاملات رسانه‌ها (Volume by Type)</b></td>
      <td style="text-align: right;">Categorical Bar Plot</td>
      <td style="text-align: right;">۱۳ امتیاز فیلم در برابر ۱۱ امتیاز کتاب</td>
      <td style="text-align: right;">توازن بسیار مطلوب بین دو رسانه؛ تضمین اینکه مدل آموزش‌دیده نهایی دچار غلبه نامتقارن یک رسانه بر دیگری (Media Bias) نخواهد شد.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>۳</b></td>
      <td style="text-align: right;"><b>نمودار جعبه‌ای نمرات (Boxplot Distribution)</b></td>
      <td style="text-align: right;">Box & Whisker Plot</td>
      <td style="text-align: right;">میانه یکسان ۴.۰ و بدون داده پرت (Outliers)</td>
      <td style="text-align: right;">همگنی ساختار توزیع بازخوردها در هر دو حوزه؛ اثبات امکان ادغام فضای ویژگی‌ها در قالب مدل توصیه‌گر ترکیبی میان‌حوزه‌ای (Cross-Domain).</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>۴</b></td>
      <td style="text-align: right;"><b>پراکندگی فعالیت کاربران (User Engagement)</b></td>
      <td style="text-align: right;">Discrete Histogram</td>
      <td style="text-align: right;">دقیقاً ۴ تعامل ثبت‌شده به ازای هر کاربر</td>
      <td style="text-align: right;">توازن کامل بازخورد کاربران اولیه؛ شرایط ایده‌آل و بدون سوگیری برای ارزیابی عادلانه عملکرد فیلترینگ مشارکتی بر پایه کاربر (User-Based CF).</td>
    </tr>
  </tbody>
</table>

---

## 🔬 جدول مقایسه تطبیقی آماری فیلم و کتاب (Cross-Domain Comparison)

تحلیل داده‌های تلفیق‌شده با متد `groupby("item_type")` در اسکریپت تحلیلی گام سوم:

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">شاخص مقایسه‌ای</th>
      <th style="text-align: right;">رسانه فیلم (Movies)</th>
      <th style="text-align: right;">رسانه کتاب (Books)</th>
      <th style="text-align: right;">تحلیل تطبیقی و استنتاج مهندسی</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>تعداد تعاملات (Interaction Count)</b></td>
      <td style="text-align: right;">۱۳ تعامل (۵۴.۲٪)</td>
      <td style="text-align: right;">۱۱ تعامل (۴۵.۸٪)</td>
      <td style="text-align: right;">توزیع کاملاً متعادل و بدون افتادن در دام کلاس نامتوازن</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>میانگین امتیازات (Mean Rating)</b></td>
      <td style="text-align: right;">۳.۹۲</td>
      <td style="text-align: right;">۴.۰۰</td>
      <td style="text-align: right;">نمرات کتاب‌ها به دلیل گزینش آگاهانه‌تر کاربران اندکی بالاتر است</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>انحراف معیار (Standard Deviation)</b></td>
      <td style="text-align: right;">۱.۱۲</td>
      <td style="text-align: right;">۱.۰۰</td>
      <td style="text-align: right;">تنوع دیدگاه و پراکندگی سلایق در بین تماشاگران فیلم بالاتر است</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>واریانس نمرات (Variance)</b></td>
      <td style="text-align: right;">۱.۲۵</td>
      <td style="text-align: right;">۱.۰۰</td>
      <td style="text-align: right;">هم‌پوشانی و ثبات بالاتر نظرات در جامعه کتاب‌خوان‌ها نسبت به فیلم‌ها</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>میانه نمرات (Median / 50%)</b></td>
      <td style="text-align: right;">۴.۰۰</td>
      <td style="text-align: right;">۴.۰۰</td>
      <td style="text-align: right;">انطباق کامل نقطه ثقل رضایت عمومی در هر دو حوزه محتوایی</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>دامنه بین‌چارکی (IQR Range)</b></td>
      <td style="text-align: right;">۳.۰۰ تا ۵.۰۰</td>
      <td style="text-align: right;">۳.۵۰ تا ۵.۰۰</td>
      <td style="text-align: right;">فشردگی ۵۰ درصد میانی امتیازهای کتاب در بازه نمرات ممتاز</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>داده‌های پرت و خارج از محدوده (Outliers)</b></td>
      <td style="text-align: right;">۰ مورد</td>
      <td style="text-align: right;">۰ مورد</td>
      <td style="text-align: right;">پایداری آماری بالا و قابلیت اتکا برای پیش‌بینی‌های مدل یادگیری</td>
    </tr>
  </tbody>
</table>

---

## 📐 فاز چهارم: مهندسی مدل‌های پایه (Baseline)، مهار تله دقت و پروتکل اعتبارسنجی (Step-4)

در گام چهارم، با هدایت نقش **طراح سیستم و معمار مدل (System & Model Designer)**، خطوط مبنای کمّی سیستم جهت پیشگیری از خطای محاسباتی تله دقت (Accuracy Trap) تدوین گردید:

### ۱. معماری و فرمولاسیون ریاضی مدل‌های پایه
1. **مدل میانگین سراسری (Global Mean Baseline - Level 0):**  
   پیش‌بینی ارزان با زمان استنتاج $O(1)$ به عنوان کف عملکرد تجربی سیستم:
   $$\hat{r}_{u,i} = \mu = \frac{1}{\vert{}R_{train}\vert{}} \sum_{(u', i') \in R_{train}} r_{u', i'}$$

2. **مدل انحرافات خطی کاربر و آیتم با منظم‌سازی L2 (User-Item Bias Baseline - Level 1):**  
   مدل‌سازی اثر تمایل فردی کاربر ($b_u$) و محبوبیت ذاتی اثر ($b_i$) نسبت به میانگین کل:
   $$\hat{r}_{u,i} = \mu + b_u + b_i$$
   $$b_u = \frac{\sum_{i \in I_u} (r_{u,i} - \mu)}{\lambda_1 + \vert{}I_u\vert{}}, \quad b_i = \frac{\sum_{u \in U_i} (r_{u,i} - \mu - b_u)}{\lambda_2 + \vert{}U_i\vert{}}$$

3. **مدل رتبه‌بندی مبتنی بر محبوبیت (Popularity-Based Top-K Baseline - Level 2):**  
   استفاده از امتیاز وزنی بیزی برای حل چالش کاربران تازه‌وارد (Cold-Start Problem).

### ۲. ماتریس هدف‌گذاری مقایسه‌ای مدل‌ها در گام چهارم

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">رده مدل</th>
      <th style="text-align: right;">نام مدل / الگوریتم</th>
      <th style="text-align: right;">شاخص RMSE (هدف)</th>
      <th style="text-align: right;">شاخص MAE (هدف)</th>
      <th style="text-align: right;">Precision@10</th>
      <th style="text-align: right;">Recall@10</th>
      <th style="text-align: right;">وضعیت فنی در گام چهارم</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>Baseline 0</b></td>
      <td style="text-align: right;">Global Mean Dummy</td>
      <td style="text-align: right;">~ ۱.۷۶</td>
      <td style="text-align: right;">~ ۱.۴۰</td>
      <td style="text-align: right;">۰.۰۴</td>
      <td style="text-align: right;">۰.۰۲</td>
      <td style="text-align: right;">طراحی و فرمول‌بندی شد (کف عملکرد)</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>Baseline 1</b></td>
      <td style="text-align: right;">User-Item Biases</td>
      <td style="text-align: right;">< ۱.۱۵</td>
      <td style="text-align: right;">< ۰.۸۵</td>
      <td style="text-align: right;">۰.۱۲</td>
      <td style="text-align: right;">۰.۰۸</td>
      <td style="text-align: right;">طراحی و فرمول‌بندی شد (مبنای مهندسی‌شده)</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>Baseline 2</b></td>
      <td style="text-align: right;">Popularity Top-K</td>
      <td style="text-align: right;">نامربوط</td>
      <td style="text-align: right;">نامربوط</td>
      <td style="text-align: right;">۰.۱۸</td>
      <td style="text-align: right;">۰.۱۱</td>
      <td style="text-align: right;">استراتژی شروع سرد</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>Collaborative</b></td>
      <td style="text-align: right;">User-Based k-NN</td>
      <td style="text-align: right;">< ۰.۹۸</td>
      <td style="text-align: right;">< ۰.۷۲</td>
      <td style="text-align: right;">> ۰.۲۴</td>
      <td style="text-align: right;">> ۰.۱۷</td>
      <td style="text-align: right;">تحویل مستندات به بخش پیاده‌سازی</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>Collaborative</b></td>
      <td style="text-align: right;">Item-Based k-NN</td>
      <td style="text-align: right;">< ۰.۹۴</td>
      <td style="text-align: right;">< ۰.۶۹</td>
      <td style="text-align: right;">> ۰.۲۶</td>
      <td style="text-align: right;">> ۰.۱۹</td>
      <td style="text-align: right;">تحویل مستندات به بخش پیاده‌سازی</td>
    </tr>
  </tbody>
</table>

---

## 🧪 بخش تکالیف و کارگاه‌های هفتگی آزمایشگاه هوش مصنوعی

کلیه تمرین‌های پنج جلسه نخست در پوشه اختصاصی `weekly_assignments/` مستندسازی و اجرا شده‌اند:

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">جلسه</th>
      <th style="text-align: right;">موضوع کارگاه هفتگی</th>
      <th style="text-align: right;">فایل پیاده‌سازی‌شده</th>
      <th style="text-align: right;">نتایج و چالش‌های انجام‌شده</th>
      <th style="text-align: right;">وضعیت</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>اول</b></td>
      <td style="text-align: right;">تست و اعتبارسنجی محیط نرم‌افزاری</td>
      <td style="text-align: right;" dir="ltr"><a href="weekly_assignments/check_env.ipynb"><code>check_env.ipynb</code></a></td>
      <td style="text-align: right;">تست پایداری NumPy, Pandas, Matplotlib, Scipy در محیط مجازی Conda</td>
      <td style="text-align: right;">تکمیل ✅</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>دوم و سوم</b></td>
      <td style="text-align: right;">مسیریابی هوشمند و الگوریتم‌های جستجو</td>
      <td style="text-align: right;" dir="ltr"><a href="weekly_assignments/lab2_pathfinding.ipynb"><code>lab2_pathfinding.ipynb</code></a></td>
      <td style="text-align: right;">مقایسه BFS, DFS و A* در ۱۰۰ نقشه تصادفی و پیاده‌سازی چالش حرکت ۸ جهته با هیوریستیک چبیشف</td>
      <td style="text-align: right;">تکمیل ✅</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>چهارم</b></td>
      <td style="text-align: right;">بازی تقابلی Nim و تحلیل EDA</td>
      <td style="text-align: right;" dir="ltr"><a href="weekly_assignments/lab3_nim_minimax_eda_graphical.ipynb"><code>lab3_nim_minimax_eda_graphical.ipynb</code></a></td>
      <td style="text-align: right;">کاهش بیش از ۹۹.۵٪ گره‌ها در هرس Alpha-Beta (ترتیب big_first)، ساخت رابط تعاملی ipywidgets و چالش Misère</td>
      <td style="text-align: right;">تکمیل ✅</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>پنجم</b></td>
      <td style="text-align: right;">یادگیری ماشین نظارت‌شده و تله دقت</td>
      <td style="text-align: right;" dir="ltr"><a href="weekly_assignments/lab4_nim_ml_sklearn.ipynb"><code>lab4_nim_ml_sklearn.ipynb</code></a></td>
      <td style="text-align: right;">اثبات تله دقت (Dummy vs k-NN)، حل کامل با متغیر بیتی nim_sum (F1=1.000) و رسم منحنی بیش‌برازش عمق درخت (tree_depth_curve.png)</td>
      <td style="text-align: right;">تکمیل ✅</td>
    </tr>
  </tbody>
</table>

---

## 🛠️ مشخصات فنی و محیط توسعه پایدار سیستم

تمامی پایپ‌لاین‌ها بر روی سیستم‌عامل ویندوز ۱۱ ویرایش ۶۴ بیتی اعتبارسنجی شده و پایداری کدهای آن به ثبت رسیده است:

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">ابزار / کتابخانه</th>
      <th style="text-align: right;">نسخه پایدار</th>
      <th style="text-align: right;">نقش در پایپ‌لاین و معماری نرم‌افزار</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>Python</b></td>
      <td style="text-align: right;" dir="ltr">3.10+ / 3.11+ / 3.14</td>
      <td style="text-align: right;">محیط اصلی مفسر و توسعه کدها</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>Scikit-Learn</b></td>
      <td style="text-align: right;" dir="ltr">1.3+ / 1.4+</td>
      <td style="text-align: right;">هسته یادگیری ماشین، مدل‌های طبقه‌بندی و محاسبه ماتریس‌های درهم‌ریختگی و شاخص‌های Precision, Recall, F1</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>Pandas</b></td>
      <td style="text-align: right;" dir="ltr">2.0+ / 3.0.5</td>
      <td style="text-align: right;">مدیریت دیتافریم‌ها، ادغام رابطه‌ای، ممیزی کیفیت و محاسبات تجمیعی</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>NumPy</b></td>
      <td style="text-align: right;" dir="ltr">1.24+ / 2.5.2</td>
      <td style="text-align: right;">محاسبات برداری سریع ریاضی، محاسبه آماره‌های توصیفی و عملیات بیتی</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>Matplotlib</b></td>
      <td style="text-align: right;" dir="ltr">3.7+ / 3.11.1</td>
      <td style="text-align: right;">رسم گرید ۴ نمودار تحلیلی، منحنی‌های بیش‌برازش و ماتریس‌های سردرگمی با کیفیت ۳۰۰ DPI</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>Jupyter Notebook / Lab</b></td>
      <td style="text-align: right;" dir="ltr">1.1.1</td>
      <td style="text-align: right;">محیط تعاملی توسعه و مصورسازی نتایج ممیزی، EDA و آموزش مدل‌ها</td>
    </tr>
  </tbody>
</table>

---

## 🚀 راهنمای نصب و راه‌اندازی سریع پروژه (Quick Start Guide)

جهت کلون‌سازی مخزن و اجرای کامل محیط ایزوله:

### ۱. دریافت مخزن از گیت‌هاب
```bash
git clone [https://github.com/ebrahimy5280-del/movie-book-recommender.git](https://github.com/ebrahimy5280-del/movie-book-recommender.git)
cd movie-book-recommender
```

### ۲. راه‌اندازی محیط مجازی با Conda یا Pip
استفاده از Conda (روش پیشنهادی):
```bash
conda env create -f movie_book_recommender_project/environment.yml
conda activate ailab
```
*یا نصب مستقیم با پکیج منیجر Pip:*
```bash
python -m pip install -r movie_book_recommender_project/requirements.txt
```

### ۳. اجرای ماژول‌ها و پایپ‌لاین‌های مراحل مختلف
```bash
# اجرای شبیه‌سازی عامل‌های هوشمند گام اول
python movie_book_recommender_project/Step-1/recommender_agent.py

# اجرای تفکیک داده و ممیزی عدم نشت گام دوم
python movie_book_recommender_project/Step-2/src/data_loader.py
python movie_book_recommender_project/Step-2/src/evaluation.py

# اجرای محیط نوت‌بوک تحلیلی EDA گام سوم
cd movie_book_recommender_project/Step-3/src
jupyter notebook eda.ipynb

# اجرای نوت‌بوک یادگیری ماشین تمرین هفتگی جلسه پنجم
cd ../../../weekly_assignments
jupyter notebook lab4_nim_ml_sklearn.ipynb
```

---

## 🗺️ نقشه راه توسعه و فازهای آتی (Project Roadmap)

- [x] **گام اول:** پیاده‌سازی و شبیه‌سازی عامل‌های سه‌گانه هوشمند (تصادفی، واکنشی، مدل‌محور) در چارچوب PEAS
- [x] **گام دوم:** معماری خط لوله تفکیک داده Train/Test، ممیزی عدم نشت و محاسبه نرخ تخلخل
- [x] **گام دوم:** تدوین سند جامع طراحی سیستم، فرمولاسیون ریاضی و معیارهای ارزیابی در `DESIGN.md`
- [x] **گام سوم:** پیاده‌سازی خط لوله تحلیل اکتشافی داده‌ها (EDA) و ممیزی سلامت داده‌ها در نوت‌بوک
- [x] **گام سوم:** طراحی بوم گرافیکی ۴ نمودار تحلیلی با کیفیت ۳۰۰ DPI و حل تعارضات کتابخانه ترسیم
- [x] **گام چهارم:** انتخاب و فرمولاسیون ریاضی مدل‌های پایه (Global Mean، Biases و Popularity) و تدوین `DESIGN.md`
- [x] **گام چهارم:** گزینش معیارهای ارزیابی آفلاین پیش‌بینی و رتبه‌بندی (RMSE, MAE, Recall@K, NDCG@K)
- [x] **تمرین‌های هفتگی:** تکمیل کامل تکالیف جلسات ۱ تا ۵ به همراه چالش‌های ۸ جهته، Misère، nim_sum و منحنی بیش‌برازش
- [ ] **گام پنجم:** پیاده‌سازی فیلترینگ مشارکتی مبتنی بر کاربر و آیتم (User-Based & Item-Based CF)
- [ ] **گام پنجم:** فاکتورگیری ماتریسی با SVD و تنظیم فراپارامترها
- [ ] **گام ششم:** پیاده‌سازی سیستم رتبه‌بندی مجدد تنوع‌محور بر پایه Maximal Marginal Relevance (MMR)
- [ ] **گام ششم:** ارزیابی نهایی مدل‌ها روی دیتاست تست با معیارهای استاندارد و مقایسه با Baselines

---

## 👤 شناسنامه پروژه و توسعه‌دهنده

- **توسعه‌دهنده:** ابراهیم یدالهی
- **درس:** آزمایشگاه هوش مصنوعی
- **ریپازیتوری اصلی گیت‌هاب:** [movie-book-recommender](https://github.com/ebrahimy5280-del/movie-book-recommender)

</div>
