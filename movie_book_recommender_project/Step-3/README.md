<div dir="rtl">

# 📊 گام سوم: تحلیل اکتشافی داده‌ها (EDA) و توسعه پایپ‌لاین تحلیلی
### 👨‍💻 پیاده‌سازی و کدنویسی: ابراهیم یدالهی

---

> 💡 **چکیده اجرایی :**  
> در این فاز از پروژه، پایپ‌لاین کامل تحلیل اکتشافی داده‌ها (Exploratory Data Analysis) برای سیستم هوشمند پیشنهاددهنده کتاب و فیلم طراحی و پیاده‌سازی گردید. این خط لوله پردازشی شامل ماژول بارگذاری پویا و چندسکویی، ممیزی خودکار شاخص‌های کیفیت داده، موتور استخراج آماره‌های توصیفی برداری، حل تعارضات کتابخانه‌های بصری‌سازی و تولید گرید گرافیکی چهارگانه با رزولوشن ۳۰۰ DPI است.

---

## 📂 ۱. ساختار ماژولار و سازمان‌دهی فایل‌ها

کلیه ورودی‌های پایگاه داده، نوت‌بوک اجرایی و فایل‌های خروجی مصورسازی‌شده طبق ساختار پوشه‌بندی زیر تفکیک و پیاده‌سازی شده‌اند:

</div>

```text
Step-3/
├── data/
│   ├── items.csv            # پایگاه داده ویژگی‌ها و متادیتای فیلم‌ها و کتاب‌ها
│   ├── ratings.csv          # لاگ بازخوردها، برچسب‌های زمانی و امتیازات کاربران
│   └── eda_analysis.png     # تصویر نهایی ۴ نمودار تحلیلی تولیدشده (DPI 300)
├── src/
│   └── eda.ipynb            # نوت‌بوک جوپیتر شامل تمام کدهای تحلیلی و آماری
└── README.md                # مستندات فنی و گزارش جامع پیاده‌سازی
```

<div dir="rtl">

---

## 🛠 ۲. شرح اقدامات و وظایف تخصصی نقش کدنویسی (توسعه‌دهنده: ابراهیم یدالهی)

به عنوان مسئول بخش پیاده‌سازی و کدنویسی نرم‌افزار در گام سوم، تسک‌های فنی و مهندسی زیر پیاده‌سازی و نهایی شدند:

- 🔹 **مدیریت مسیردهی پویا و چندسکویی (OS-Agnostic File Pathing):** به‌کارگیری کلاس `pathlib.Path` جهت تعریف مسیرهای داده به‌صورت شیءگرا و نسبی، به منظور تضمین اجرای اسکریپت بدون خطا در هر دو سیستم‌عامل ویندوز و لینوکس.
- 🔹 **ادغام رابطه‌ای مجموعه‌داده‌ها (Relational Joining Pipeline):** پیاده‌سازی عملیات Inner Join بر روی ستون یکتای `item_id` با متد بهینه `pd.merge` برای تحلیل هم‌بستگی میان فرمت رسانه و سطح امتیازها.
- 🔹 **توسعه پایپ‌لاین ممیزی سلامت داده (Automated Data Quality Audit):** کدنویسی اعتبارسنجی جامع برای تشخیص مقادیر مفقود، ردیابی سطرهای تکراری و اعتبارسنجی نوع فیلدها (`dtypes`).
- 🔹 **موتور استخراج آماره‌های توصیفی برداری (Vectorized Descriptive Engine):** استخراج کمیت‌های مرکزی و پراکندگی (میانگین، واریانس، انحراف معیار، میانه، کمینه، بیشینه و چارک‌ها) بدون استفاده از حلقه‌های کند پایتونی.
- 🔹 **برطرف‌سازی باگ ناسازگاری نسخه جدید Matplotlib:** رفع خطای تغییرات ساختاری نگارش‌های اخیر Matplotlib در نمودار جعبه‌ای (`boxplot`) با جایگزینی شیوه سنتی و مقداردهی مستقیم به متدهای `set_xticks` و `set_xticklabels` روی آبجکت‌های Axes.
- 🔹 **طراحی بوم گرافیکی چهارگانه هم‌زمان (2×2 Subplots Canvas):** پیاده‌سازی گرید بصری منسجم در ابعاد ۱۲×۸ اینچ با استایل مدرن `seaborn-v0_8-whitegrid` و بهینه‌سازی فاصله‌گذاری المان‌ها با `plt.tight_layout`.
- 🔹 **اتوماسیون خروجی گرافیکی (Export Engine):** کدنویسی ذخیره‌سازی خودکار نمودار با متد `plt.savefig` در رزولوشن ۳۰۰ DPI با برش حواشی اضافی (`bbox_inches='tight'`) در پوشه مقصد.

---

## 📋 ۳. ممیزی جامع سلامت و کیفیت داده‌ها (Data Quality Audit)

پیش از ورود به تحلیل‌های ریاضی، ارزیابی کیفی داده‌ها توسط توابع کنترلی انجام شد که نتایج آن در جدول زیر خلاصه شده است:

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">مشخصه ممیزی (Audit Metric)</th>
      <th style="text-align: right;">متد پایتون پیاده‌سازی‌شده</th>
      <th style="text-align: right;">وضعیت در ratings.csv</th>
      <th style="text-align: right;">وضعیت در items.csv</th>
      <th style="text-align: right;">وضعیت نهایی</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>ابعاد ماتریس داده</b></td>
      <td style="text-align: right;" dir="ltr"><code>df.shape</code></td>
      <td style="text-align: right;">۲۴ سطر و ۵ ستون</td>
      <td style="text-align: right;">۸ سطر و ۵ ستون</td>
      <td style="text-align: right;">✔️ منطبق با طراحی اولیه</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>مقادیر گمشده (Missing Values)</b></td>
      <td style="text-align: right;" dir="ltr"><code>df.isna().sum().sum()</code></td>
      <td style="text-align: right;">۰ مقدار نال</td>
      <td style="text-align: right;">۰ مقدار نال</td>
      <td style="text-align: right;">✔️ داده‌ها ۱۰۰٪ کامل</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>سطرهای تکراری (Duplicates)</b></td>
      <td style="text-align: right;" dir="ltr"><code>df.duplicated().sum()</code></td>
      <td style="text-align: right;">۰ ردیف تکراری</td>
      <td style="text-align: right;">۰ ردیف تکراری</td>
      <td style="text-align: right;">✔️ بدون افزونگی داده‌ای</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>صحت نوع داده شناسه کاربر</b></td>
      <td style="text-align: right;" dir="ltr"><code>df['user_id'].dtype</code></td>
      <td style="text-align: right;">رشته متنی (<code>object</code>)</td>
      <td style="text-align: right;">نامربوط</td>
      <td style="text-align: right;">✔️ استاندارد کلید اصلی</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>صحت نوع داده شناسه آیتم</b></td>
      <td style="text-align: right;" dir="ltr"><code>df['item_id'].dtype</code></td>
      <td style="text-align: right;">رشته متنی (<code>object</code>)</td>
      <td style="text-align: right;">رشته متنی (<code>object</code>)</td>
      <td style="text-align: right;">✔️ استاندارد کلید خارجی</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>صحت نوع داده امتیاز</b></td>
      <td style="text-align: right;" dir="ltr"><code>df['rating'].dtype</code></td>
      <td style="text-align: right;">عدد صحیح (<code>int64</code>)</td>
      <td style="text-align: right;">نامربوط</td>
      <td style="text-align: right;">✔️ آماده محاسبات ریاضی</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>صحت برچسب زمانی</b></td>
      <td style="text-align: right;" dir="ltr"><code>df['timestamp'].dtype</code></td>
      <td style="text-align: right;">عدد صحیح (<code>int64</code>)</td>
      <td style="text-align: right;">نامربوط</td>
      <td style="text-align: right;">✔️ استاندارد Unix Epoch</td>
    </tr>
  </tbody>
</table>

---

## 📈 ۴. خلاصه شاخص‌های آمار توصیفی نمرات (Descriptive Statistics)

تحلیل آماری انجام‌شده روی کل نمرات ثبت‌شده به شرح جدول زیر است:

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">شاخص آماری (Statistic)</th>
      <th style="text-align: right;">نماد ریاضی</th>
      <th style="text-align: right;">مقدار عددی</th>
      <th style="text-align: right;">تفسیر و مفهوم فنی در تحلیل داده</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>تعداد کل امتیازها (Count)</b></td>
      <td style="text-align: right;">$N$</td>
      <td style="text-align: right;">۲۴</td>
      <td style="text-align: right;">حجم کل تعاملات ورودی ثبت‌شده در فاز پایلوت</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>میانگین حسابی (Mean)</b></td>
      <td style="text-align: right;">$\mu$</td>
      <td style="text-align: right;">۳.۹۶</td>
      <td style="text-align: right;">تمایل عمومی و مرکز ثقل بازخورد کاربران</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>انحراف معیار (Standard Deviation)</b></td>
      <td style="text-align: right;">$\sigma$</td>
      <td style="text-align: right;">۱.۰۴</td>
      <td style="text-align: right;">فاصله میانگین نظرات کاربران حول مقدار مرکزی</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>واریانس (Variance)</b></td>
      <td style="text-align: right;">$\sigma^2$</td>
      <td style="text-align: right;">۱.۰۹</td>
      <td style="text-align: right;">توان دوم انحراف معیار و شدت پراکندگی امتیازها</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>میانه نمرات (Median / 50%)</b></td>
      <td style="text-align: right;">$Q_2$</td>
      <td style="text-align: right;">۴.۰۰</td>
      <td style="text-align: right;">نمره میانی؛ نشان‌دهنده رضایت عمومی کاربران</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>کمینه نمره (Minimum)</b></td>
      <td style="text-align: right;">$Min$</td>
      <td style="text-align: right;">۲.۰۰</td>
      <td style="text-align: right;">پایین‌ترین امتیاز ثبت‌شده در سیستم تعاملات</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>چارک اول (25th Percentile)</b></td>
      <td style="text-align: right;">$Q_1$</td>
      <td style="text-align: right;">۳.۰۰</td>
      <td style="text-align: right;">مرز ۲۵ درصد پایین نمرات داده‌شده</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>چارک سوم (75th Percentile)</b></td>
      <td style="text-align: right;">$Q_3$</td>
      <td style="text-align: right;">۵.۰۰</td>
      <td style="text-align: right;">مرز نمرات فوق‌العاده بالا و بازخوردهای عالی</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>دامنه بین‌چارکی (IQR)</b></td>
      <td style="text-align: right;">$Q_3 - Q_1$</td>
      <td style="text-align: right;">۲.۰۰</td>
      <td style="text-align: right;">تمرکز ۵۰ درصد میانی نظرات کاربران</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>بیشینه نمره (Maximum)</b></td>
      <td style="text-align: right;">$Max$</td>
      <td style="text-align: right;">۵.۰۰</td>
      <td style="text-align: right;">سقف امتیاز سیستم پیشنهاددهنده</td>
    </tr>
  </tbody>
</table>

---

## ⚖️ ۵. جدول مقایسه تحلیلی فیلم در برابر کتاب (Cross-Domain Comparison)

برای درک رفتار کاربران در هر رسانه، داده‌ها با متد `groupby("item_type")` تفکیک و مقایسه گردیدند:

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">شاخص مقایسه‌ای</th>
      <th style="text-align: right;">رسانه فیلم (Movies)</th>
      <th style="text-align: right;">رسانه کتاب (Books)</th>
      <th style="text-align: right;">تحلیل و مقایسه تطبیقی</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>حجم تعاملات (Interaction Count)</b></td>
      <td style="text-align: right;">۱۳ تعامل (۵۴.۲٪)</td>
      <td style="text-align: right;">۱۱ تعامل (۴۵.۸٪)</td>
      <td style="text-align: right;">توازن بسیار عالی بین دو رسانه بدون چولگی حجمی</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>میانگین نمرات (Mean Rating)</b></td>
      <td style="text-align: right;">۳.۹۲</td>
      <td style="text-align: right;">۴.۰۰</td>
      <td style="text-align: right;">نمرات کتاب‌ها به میزان ۰.۰۸ واحد بالاتر است</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>انحراف معیار (Standard Deviation)</b></td>
      <td style="text-align: right;">۱.۱۲</td>
      <td style="text-align: right;">۱.۰۰</td>
      <td style="text-align: right;">نظرات فیلم‌ها تنوع و پراکندگی بیشتری نسبت به کتاب دارند</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>واریانس نمرات (Variance)</b></td>
      <td style="text-align: right;">۱.۲۵</td>
      <td style="text-align: right;">۱.۰۰</td>
      <td style="text-align: right;">هم‌گرایی بیشتر آراء در دسته کتاب‌ها نسبت به فیلم</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>میانه نمرات (Median)</b></td>
      <td style="text-align: right;">۴.۰۰</td>
      <td style="text-align: right;">۴.۰۰</td>
      <td style="text-align: right;">انطباق کامل نقطه ثقل رضایت در هر دو رسانه</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>چارک اول و سوم (IQR Range)</b></td>
      <td style="text-align: right;">۳.۰۰ تا ۵.۰۰</td>
      <td style="text-align: right;">۳.۵۰ تا ۵.۰۰</td>
      <td style="text-align: right;">فشردگی بیشتر ۵۰ درصد میانی امتیازات کتاب‌ها</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>داده پرت و نامتعارف (Outliers)</b></td>
      <td style="text-align: right;">۰ مورد</td>
      <td style="text-align: right;">۰ مورد</td>
      <td style="text-align: right;">رفتار آماری کاملاً همگن و قابل اطمینان</td>
    </tr>
  </tbody>
</table>

---

## 🎨 ۶. مهندسی مصورسازی داده‌ها و تشریح نمودارها

خروجی تصویری تولیدشده توسط پایپ‌لاین که در مسیر `data/eda_analysis.png` ذخیره شده است:

<div align="center">

![نمودارهای تحلیل اکتشافی داده‌ها](data/eda_analysis.png)

</div>

### 1️⃣ توزیع فراوانی نمرات (Rating Distribution)
- **نوع و ساختار پیاده‌سازی:** Bar Plot / Frequency Histogram با مرتب‌سازی اندیس‌ها.
- **جزئیات و تحلیل فنی:** نمرات ۲، ۳، ۴ و ۵ به ترتیب دارای فراوانی ۳، ۴، ۸ و ۹ هستند. تمرکز بیش از ۷۰ درصدی داده‌ها روی سطوح رضایت بالا نشان‌دهنده چولگی منفی (Left-skewed) و وجود پدیده سوگیری مثبت (Positivity Bias) در بازخوردهای کاربران است.

### 2️⃣ حجم تعاملات به تفکیک رسانه (Interaction Volume by Media Type)
- **نوع و ساختار پیاده‌سازی:** Categorical Bar Plot با پالت رنگی مجزا برای هر دسته.
- **جزئیات و تحلیل فنی:** نسبت ۱۳ فیلم به ۱۱ کتاب اثبات می‌کند که دیتاست دارای بالانس بسیار خوبی است و مدل توصیه‌گر دچار انحراف ناشی از عدم تقارن کلاس‌ها (Class Imbalance) نخواهد شد.

### 3️⃣ مقایسه آماری نمرات رسانه‌ها (Boxplot Distribution)
- **نوع و ساختار پیاده‌سازی:** Box & Whisker Plot با مشخص کردن میانه قرمز رنگ و خطوط چارکی.
- **جزئیات و تحلیل فنی:** خط میانه در هر دو رسانه روی عدد ۴.۰ ثابت است. بازه بین‌چارکی کتاب‌ها فشرده‌تر بوده و نبود نقاط خارج از خطوط ویسکرز نشان‌دهنده نبود داده پرت حاد در هر دو حوزه رسانه‌ای است.

### 4️⃣ پراکندگی حجم فعالیت کاربران (User Engagement Dispersion)
- **نوع و ساختار پیاده‌سازی:** Discrete Histogram با باین‌بندی دقیق داده‌ها.
- **جزئیات و تحلیل فنی:** تمام ۶ کاربر ثبت‌شده در پایگاه داده دقیقاً دارای ۴ تعامل هستند. این تقارن، شرایطی ایده‌آل برای ارزیابی الگوریتم‌های فیلترینگ مشارکتی بر پایه کاربر (User-Based CF) بدون اخلال پدیده کاربران کم‌تعامل فراهم می‌آورد.

---

## 🎯 ۷. خلاصه تحلیلی نتایج در قالب مشاهده، دلیل و نتیجه

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">مشاهده (Observation)</th>
      <th style="text-align: right;">ریشه و دلیل داده‌ای (Reason)</th>
      <th style="text-align: right;">نتیجه در سیستم پیشنهاددهنده (Conclusion)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>۷۰.۸٪ نمرات در سطوح ۴ و ۵ ثبت شده‌اند.</b></td>
      <td style="text-align: right;">سوگیری مثبت بازخورد؛ کاربران بیشتر تمایل به ثبت بازخورد روی آثاری دارند که مورد پسندشان واقع شده است.</td>
      <td style="text-align: right;">در فاز مدل‌سازی، نرمال‌سازی انحراف از میانگین (Mean-Centering) برای حذف سوگیری خوش‌بینی یا سخت‌گیری کاربران ضروری است.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>میانگین نمرات کتاب (۴.۰۰) کمی بالاتر از فیلم (۳.۹۲) است.</b></td>
      <td style="text-align: right;">مطالعه کتاب نیاز به صرف زمان بیشتری دارد و کاربران در گزینش اولیه کتاب‌ها دقت بالاتری به خرج می‌دهند.</td>
      <td style="text-align: right;">رفتار بازخوردی هر دو رسانه بسیار نزدیک و همگن است و می‌توان از یک ساختار پیشنهادی مشترک (Cross-Domain) استفاده کرد.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>میانه نمرات (۴.۰۰) از میانگین (۳.۹۶) بالاتر است.</b></td>
      <td style="text-align: right;">وجود چند نمره ضعیف (امتیاز ۲) میانگین حسابی را اندکی به سمت پایین متمایل کرده است.</td>
      <td style="text-align: right;">میانه به عنوان شاخص مرکزی ناپارامتری، معیار باثبات‌تری برای تعریف آستانه رضایت کاربران محسوب می‌شود.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>تمامی کاربران دارای دقیقاً ۴ تعامل ثبت‌شده هستند.</b></td>
      <td style="text-align: right;">فرآیند تولید کنترل‌شده و ساختاریافته داده‌های اعتبارسنجی اولیه در گام دوم.</td>
      <td style="text-align: right;">ماتریس تعاملات در این مرحله چالش تنک‌بودن نامتقارن ندارد و پایپ‌لاین مدل‌سازی بدون خطای مقادیر تهی تست خواهد شد.</td>
    </tr>
  </tbody>
</table>

---

## 🚀 ۸. راهنمای گام‌به‌گام راه‌اندازی و اجرای خط لوله

برای بازتولید کلیه خروجی‌ها و اجرای مجدد محاسبات در محیط ترمینال و جوپیتر:

۱. فعال‌سازی محیط کاندای اختصاصی پروژه:
```bash
conda activate ailab
```

۲. ورود به پوشه کدهای گام سوم:
```bash
cd movie_book_recommender_project/Step-3/src
```

۳. اجرای نوت‌بوک جوپیتر:
```bash
jupyter notebook eda.ipynb
```

با اجرای سلول‌های نوت‌بوک، جدول‌های ممیزی و خروجی‌های آماری در کنسول چاپ شده و تصویر ۴ نمودار تحلیلی با کیفیت بالا در مسیر `Step-3/data/eda_analysis.png` به‌صورت خودکار ذخیره و جایگزین می‌شود.

</div>
