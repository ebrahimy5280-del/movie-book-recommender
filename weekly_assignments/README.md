<div dir="rtl" align="right">

# 📚 تمرین‌ها و تکالیف هفتگی آزمایشگاه هوش مصنوعی

**تهیه‌کننده: ابراهیم یدالهی**  
**درس:** آزمایشگاه هوش مصنوعی  
**محیط اجرا:** پایتون، Conda (`ailab`) و نوت‌بوک تعاملی ژوپیتر

این مخزن شامل کلیه تمرین‌های عملی، فعالیت‌های کارگاهی، پروژه‌های هفتگی و نوت‌بوک‌های تحلیلی جلسات آزمایشگاه هوش مصنوعی است. ساختار فایل‌ها، کدهای پیاده‌سازی‌شده و مستندات تحلیلی هر جلسه به تفکیک به شرح زیر تدوین شده است:

---

## 🗓 فهرست جلسات و فایل‌ها

### ۱. جلسه اول: آماده‌سازی و اعتبارسنجی محیط توسعه
- **فایل:** `check_env.ipynb`
- **شرح تفصیلی:** راه‌اندازی و اعتبارسنجی محیط پایه کلاسی پایتون و ابزارهای موردنیاز، شامل تست و بررسی نصب بودن صحیح کتابخانه‌های اصلی پردازش داده و یادگیری ماشین (نظیر `numpy`، `pandas`، `matplotlib` و `scipy`)، سنجش نسخه‌ها و حصول اطمینان از عملکرد بستر ایزوله Conda (`ailab`).

---

### ۲. جلسات دوم و سوم: پیاده‌سازی و مقایسه الگوریتم‌های جستجو و مسیریابی
- **فایل:** `lab2_pathfinding.ipynb`
- **شرح تفصیلی:** پیاده‌سازی مسئله حرکت عامل هوشمند (ربات) در محیط مشبک دوبعدی (Grid) با موانع تصادفی. مقایسه جامع عملکرد، پیچیدگی زمانی و حافظه‌ای الگوریتم‌های جستجوی ناآگاهانه (`BFS` و `DFS`) در مقایسه با الگوریتم آگاهانه (`A*` بر پایه هیوریستیک فاصله منهتن) در ۱۰۰ نقشه تصادفی مختلف، ارزیابی طول مسیر و تعداد سلول‌های گسترش‌یافته، پاسخ تشریحی به رفتار الگوریتم‌ها و پیاده‌سازی چالش تکمیلی حرکت ۸ جهته با هیوریستیک فاصله چبیشف (Chebyshev Distance).

---

### ۳. جلسه چهارم: بازی Nim با جستجوی تقابلی (Minimax و هرس Alpha-Beta) و تحلیل EDA
- **فایل:** `lab3_nim_minimax_eda_graphical.ipynb`
- **شرح تفصیلی:** مدل‌سازی بازی ریاضی نیم (Nim) با دو بازیکن A (بیشینه‌ساز / MAX) و B (کمینه‌ساز / MIN) در قالب جستجوی تقابلی دو نفره، نوبتی و مجموع صفر. پیاده‌سازی و مقایسه گره‌های پیمایش‌شده الگوریتم Minimax کامل در برابر هرس آلفا-بتا (با ترتیب پیش‌فرض و بهینه `big_first`)، استخراج پایگاه داده ۲۰۰ بازی شبیه‌سازی‌شده و ممیزی سلامت داده‌ها، رندرسازی گرید ۴ نمودار تحلیلی، ساخت رابط کاربری گرافیکی تعاملی انسان در برابر کامپیوتر با ابزارک‌های `ipywidgets` و اجرای چالش تکمیلی قانون معکوس (Misère Nim Rule).

---

### ۴. جلسه پنجم: یادگیری نظارت‌شده، ارزیابی مدل‌ها و تله دقت روی بازی Nim
- **فایل:** `lab4_nim_ml_sklearn.ipynb`
- **شرح تفصیلی:** فرمولاسیون مسئله یادگیری نظارت‌شده (Supervised Learning) برای پیش‌بینی وضعیت بازنده (`loses = True`) در ۵۱۲ وضعیت ممکن بازی Nim با ۳ پشته سنگ (از ۰ تا ۷ سنگ). این تمرین در دو بخش کلی توسعه یافته است:
  1. **بخش اول (دستی با NumPy):** تفکیک داده‌ها به ۷۰٪ آموزش و ۳۰٪ آزمون، پیاده‌سازی مدل پایه Dummy Baseline، الگوریتم k-NN از صفر با فاصله منهتن و محاسبه ماتریس درهم‌ریختگی (Confusion Matrix) و معیارهای Accuracy، Precision و Recall بدون کتابخانه جانبی.
  2. **بخش دوم (با Scikit-Learn و مهندسی ویژگی):** پیاده‌سازی و مقایسه ۴ مدل (Baseline، k-NN، درخت تصمیم و رگرسیون لجستیک)، اثبات تجربی تله دقت (Accuracy Trap) روی داده‌های نامتوازن، مهندسی ویژگی با ایجاد متغیر بیتی `nim_sum` ($p_1 \oplus p_2 \oplus p_3$) و جهش عملکرد مدل‌ها به ۱۰۰٪.
  3. **چالش‌های توسعه:** ارزیابی کلیه مدل‌ها با معیار $F_1\text{-Score}$، اجرای تحلیل بیش‌برازش (Overfitting) با تغییر عمق درخت تصمیم (`max_depth` از ۱ تا ۱۰) روی داده‌های خام و خروجی‌گیری نمودار تحلیلی با کیفیت بالا (`tree_depth_curve.png`).

---

## 📊 جدول مشخصات و وضعیت تحویل تمرین‌ها

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">جلسه</th>
      <th style="text-align: right;">عنوان تمرین</th>
      <th style="text-align: right;">نام فایل در مخزن</th>
      <th style="text-align: right;">مفاهیم کلیدی پیاده‌سازی‌شده</th>
      <th style="text-align: right;">وضعیت تحویل</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>اول</b></td>
      <td style="text-align: right;">بررسی محیط نرم‌افزاری</td>
      <td style="text-align: right;" dir="ltr"><a href="check_env.ipynb"><code>check_env.ipynb</code></a></td>
      <td style="text-align: right;">پایتون، پکیج‌ها، اعتبارسنجی وابستگی‌های محیطی</td>
      <td style="text-align: right;">تکمیل ✅</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>دوم و سوم</b></td>
      <td style="text-align: right;">مسیریابی و الگوریتم‌های جستجو</td>
      <td style="text-align: right;" dir="ltr"><a href="lab2_pathfinding.ipynb"><code>lab2_pathfinding.ipynb</code></a></td>
      <td style="text-align: right;">BFS, DFS, A*, هیوریستیک منهتن، چالش حرکت ۸ جهته</td>
      <td style="text-align: right;">تکمیل ✅</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>چهارم</b></td>
      <td style="text-align: right;">بازی نیم، Minimax، هرس و EDA</td>
      <td style="text-align: right;" dir="ltr"><a href="lab3_nim_minimax_eda_graphical.ipynb"><code>lab3_nim_minimax_eda_graphical.ipynb</code></a></td>
      <td style="text-align: right;">Minimax, Alpha-Beta Pruning, EDA, ipywidgets GUI, Misère Challenge</td>
      <td style="text-align: right;">تکمیل ✅</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>پنجم</b></td>
      <td style="text-align: right;">یادگیری ماشین، تله دقت و بازی نیم</td>
      <td style="text-align: right;" dir="ltr"><a href="lab4_nim_ml_sklearn.ipynb"><code>lab4_nim_ml_sklearn.ipynb</code></a></td>
      <td style="text-align: right;">Supervised Learning, k-NN, Decision Tree, Logistic Regression, nim_sum, F1-Score, Overfitting Curve</td>
      <td style="text-align: right;">تکمیل ✅</td>
    </tr>
  </tbody>
</table>

---

## 🔬 بخش اول: جزئیات و برون‌دادهای تحلیلی تمرین جلسه چهارم (بازی Nim با جستجوی تقابلی)

### ۱. مقایسه هزینه محاسباتی الگوریتم‌های جستجو
برای پشته کلاسیک شروع `(3, 4, 5)`، تعداد گره‌های پیمایش‌شده به شرح زیر ارزیابی گردید:
- **الگوریتم Minimax کامل:** بررسی **۱٬۰۳۸٬۷۶۸ گره** (بررسی تمامی انشعاب‌های درخت بازی)
- **الگوریتم Alpha-Beta (ترتیب پیش‌فرض):** بررسی **۳۳٬۹۱۶ گره**
- **الگوریتم Alpha-Beta (ترتیب بهینه `big_first`):** بررسی **۴٬۳۳۲ گره** (کاهش بیش از ۹۹.۵ درصدی محاسبات نسبت به مینی‌مکس)

---

### ۲. جدول تفسیر تحلیلی داده‌های بازی نیم (مشاهده ⬅️ دلیل ⬅️ نتیجه)

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">مشاهده (Observation)</th>
      <th style="text-align: right;">ریشه و دلیل داده‌ای (Reason)</th>
      <th style="text-align: right;">نتیجه در نظریه بازی‌ها (Conclusion)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>بازیکن A در ۸۸٪ شروع‌ها برنده است.</b></td>
      <td style="text-align: right;">در بیشتر حالات شروع تصادفی، مقدار <code>nim_sum</code> مخالف صفر است.</td>
      <td style="text-align: right;">بازی نیم در صورت بازی بدون خطا، برتری قطعی را به بازیکن اول اعطا می‌کند.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>تطابق ۱۰۰ درصدی برنده شدن با <code>nim_sum != 0</code>.</b></td>
      <td style="text-align: right;">قضیه ریاضی بوتون (Bouton's Theorem) بر مبنای حاصل جمع بیتی XOR اندازه پشته‌ها.</td>
      <td style="text-align: right;">پاسخ تحلیلی Minimax کاملاً با منطق تئوری جبر بولی مطابقت دارد و درستی پیاده‌سازی اثبات شد.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>هرس آلفا-بتا تنها ۲.۵٪ گره‌های Minimax را پیمایش کرد.</b></td>
      <td style="text-align: right;">قطع شاخه‌های بی‌اثر با برقراری شرط هرس $\alpha \ge \beta$.</td>
      <td style="text-align: right;">بدون افت کیفیت خروجی، هزینه زمانی و حافظه‌ای الگوریتم چندین مرتبه کاهش یافت.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>میانگین گره‌ها (۳۸٬۵۱۵) از میانه (۴٬۳۴۸) بسیار بزرگ‌تر است.</b></td>
      <td style="text-align: right;">چند شروع سنگین با مجموع سنگ‌های زیاد، توزیع داده‌ها را دارای چولگی شدید به راست کرده‌اند.</td>
      <td style="text-align: right;">برای توصیف واقع‌بینانه هزینه جستجو، میانه و مقیاس لگاریتمی بسیار دقیق‌تر از میانگین هستند.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>ثبت ۱۰۹ سطر تکراری در میان ۲۰۰ بازی شبیه‌سازی‌شده.</b></td>
      <td style="text-align: right;">فضای نمونه برای ۳ پشته با اندازه ۱ تا ۴ تنها ۶۴ حالت یکتا دارد.</td>
      <td style="text-align: right;">تکرار سطرها در این محیط کاملاً طبیعی است و به معنی خطای ثبت داده نیست.</td>
    </tr>
  </tbody>
</table>

---

### ۳. چالش توسعه‌یافته: قانون معکوس (Misère Play)
در انتهای نوت‌بوک، تابع `minimax_misere` پیاده‌سازی گردید که در آن شرط پایان معکوس شده است؛ بازیکنی که آخرین سنگ را بردارد بازنده اعلام می‌شود. با اجرای این تابع برای حالت شروع `(1, 2, 3)`، خروجی مقدار `-1` به دست آمد که نشان می‌دهد بازیکن دوم (B) در بازی معکوس برنده است.

---

## 🔬 بخش دوم: جزئیات و نتایج تحلیلی تمرین جلسه پنجم (یادگیری ماشین و نوت‌بوک Lab 4)

### ۱. ارزیابی اولیه مدل‌ها با ویژگی‌های خام (نمایش تله دقت)
در این آزمایش با ویژگی‌های خام $p_1, p_2, p_3$، عملکرد مدل‌ها روی داده آزمون ($30\%$) به شرح زیر است:
- **مدل پایه (Dummy Baseline - همواره پیش‌بینی برد):** دقت $0.877$، ضریب Recall برابر $0.000$
- **مدل k-NN دستی و آماده ($k=3$):** دقت $0.760$، ضریب Recall برابر $0.000$ (بدتر از Baseline!)
- **مدل درخت تصمیم (Decision Tree):** دقت $0.734$، ضریب Recall برابر $0.000$
- **ماتریس درهم‌ریختگی مدل k-NN دستی:**  
  $\text{TP}=0 \quad | \quad \text{FP}=14 \quad | \quad \text{FN}=18 \quad | \quad \text{TN}=122$  
  *(مدل حتی یک وضعیت بازنده واقعی را هم پیدا نکرده است؛ این مسئله تله دقت را اثبات می‌کند).*

---

### ۲. جدول نتایج نهایی مدل‌ها با معیار $F_1$ (پس از مهندسی ویژگی با `nim_sum`)

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">الگوریتم / مدل</th>
      <th style="text-align: right;">Accuracy</th>
      <th style="text-align: right;">Precision</th>
      <th style="text-align: right;">Recall</th>
      <th style="text-align: right;">F1-Score</th>
      <th style="text-align: right;">تحلیل عملکرد و رفتار مدل</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>baseline (always wins)</b></td>
      <td style="text-align: right;">۰.۸۷۷</td>
      <td style="text-align: right;">۰.۰۰۰</td>
      <td style="text-align: right;">۰.۰۰۰</td>
      <td style="text-align: right;">۰.۰۰۰</td>
      <td style="text-align: right;">پیش‌بینی یکنواخت کلاس پرتکرار بدون یادگیری واقعی</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>k-NN (k=3)</b></td>
      <td style="text-align: right;">۰.۹۴۲</td>
      <td style="text-align: right;">۰.۷۰۸</td>
      <td style="text-align: right;">۰.۸۹۵</td>
      <td style="text-align: right;">۰.۷۹۱</td>
      <td style="text-align: right;">تفکیک‌پذیری چشمگیر نقاط با اضافه شدن بعد XOR</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>decision tree</b></td>
      <td style="text-align: right;">۱.۰۰۰</td>
      <td style="text-align: right;">۱.۰۰۰</td>
      <td style="text-align: right;">۱.۰۰۰</td>
      <td style="text-align: right;">۱.۰۰۰</td>
      <td style="text-align: right;">انشعاب در ریشه با شرط <code>nim_sum == 0</code> و حل کامل مسئله</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>logistic regression</b></td>
      <td style="text-align: right;">۱.۰۰۰</td>
      <td style="text-align: right;">۱.۰۰۰</td>
      <td style="text-align: right;">۱.۰۰۰</td>
      <td style="text-align: right;">۱.۰۰۰</td>
      <td style="text-align: right;">جداسازی کامل خطی داده‌ها در فضای ویژگی ارتقایافته</td>
    </tr>
  </tbody>
</table>

---

### ۳. جدول تفسیر تحلیلی یادگیری ماشین در بازی نیم (مشاهده ⬅️ دلیل ⬅️ نتیجه)

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">مشاهده (Observation)</th>
      <th style="text-align: right;">دلیل علمی و داده‌ای (Reason)</th>
      <th style="text-align: right;">نتیجه‌گیری و تصمیم مهندسی (Conclusion)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>مدل Baseline دقت ۸۷.۷٪ دارد ولی Recall آن صفر است.</b></td>
      <td style="text-align: right;">۸۷.۵٪ داده‌ها متعلق به کلاس برد هستند و مدل ساده همواره کلاس اکثریت را حدس می‌زند.</td>
      <td style="text-align: right;">معیار Accuracy برای داده‌های نامتوازن به‌تنهایی گمراه‌کننده است و باید از Recall و F1-Score استفاده شود.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>مدل‌های k-NN و درخت تصمیم با ویژگی‌های خام از Baseline ضعیف‌ترند.</b></td>
      <td style="text-align: right;">قانون بازی Nim تابعی از عملگر بیتی XOR است که با فاصله اقلیدسی یا منهتن خام تفکیک خطی ندارد.</td>
      <td style="text-align: right;">الگوریتم یادگیری نمی‌تواند ضعف ناشی از بازنمایی نامناسب داده‌ها را جبران کند.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>افزودن متغیر <code>nim_sum</code> دقت درخت تصمیم و لجستیک را به ۱۰۰٪ رساند.</b></td>
      <td style="text-align: right;">ویژگی $p_1 \oplus p_2 \oplus p_3$ مستقیماً شرط باخت بازی را در قالب یک متغیر خطی جداپذیر ارائه می‌دهد.</td>
      <td style="text-align: right;">مهندسی ویژگی (Feature Engineering) بر ارتقای پیچیدگی معماری مدل ارجحیت دارد.</td>
    </tr>
  </tbody>
</table>

---

### ۴. نتایج تجربی چالش توسعه: تحلیل بیش‌برازش در عمق درخت (`max_depth`)
در این چالش، با تغییر `max_depth` از ۱ تا ۱۰ روی ویژگی‌های خام، رفتار درخت تصمیم بررسی و تصویر `tree_depth_curve.png` استخراج گردید:

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">عمق (max_depth)</th>
      <th style="text-align: right;">دقت آموزش (Train Acc)</th>
      <th style="text-align: right;">دقت آزمون (Test Acc)</th>
      <th style="text-align: right;">Test Recall</th>
      <th style="text-align: right;">وضعیت برازش (Fitting Status)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;">۱ تا ۳</td>
      <td style="text-align: right;">۰.۸۷۴</td>
      <td style="text-align: right;">۰.۸۷۷</td>
      <td style="text-align: right;">۰.۰</td>
      <td style="text-align: right;">کم‌برازش (Underfitting - مشابه Baseline)</td>
    </tr>
    <tr>
      <td style="text-align: right;">۴ تا ۶</td>
      <td style="text-align: right;">۰.۸۷۷</td>
      <td style="text-align: right;">۰.۸۷۰</td>
      <td style="text-align: right;">۰.۰</td>
      <td style="text-align: right;">آغاز شکاف میان دقت آموزش و آزمون</td>
    </tr>
    <tr>
      <td style="text-align: right;">۷</td>
      <td style="text-align: right;">۰.۸۸۵</td>
      <td style="text-align: right;">۰.۸۴۴</td>
      <td style="text-align: right;">۰.۰</td>
      <td style="text-align: right;">کاهش تعمیم‌پذیری مدل</td>
    </tr>
    <tr>
      <td style="text-align: right;">۸</td>
      <td style="text-align: right;">۰.۹۰۵</td>
      <td style="text-align: right;">۰.۸۱۸</td>
      <td style="text-align: right;">۰.۰</td>
      <td style="text-align: right;">افت شدید دقت روی داده آزمون</td>
    </tr>
    <tr>
      <td style="text-align: right;">۹</td>
      <td style="text-align: right;">۰.۹۲۲</td>
      <td style="text-align: right;">۰.۷۷۳</td>
      <td style="text-align: right;">۰.۰</td>
      <td style="text-align: right;">بیش‌برازش چشمگیر</td>
    </tr>
    <tr>
      <td style="text-align: right;">۱۰</td>
      <td style="text-align: right;">۰.۹۴۷</td>
      <td style="text-align: right;">۰.۷۴۰</td>
      <td style="text-align: right;">۰.۰</td>
      <td style="text-align: right;">بیش‌برازش شدید (Severe Overfitting)</td>
    </tr>
  </tbody>
</table>

- **تفسیر نمودار بیش‌برازش:** با افزایش عمق به ۱۰، دقت روی داده آموزش تا **۹۴.۷٪** بالا می‌رود، اما دقت آزمون با روندی نزولی تا **۷۴.۰٪** سقوط می‌کند و ضریب Recall در تمامی عمق‌ها روی **۰.۰** باقی می‌ماند. این پدیده اثبات می‌کند که درخت تصمیم در غیاب ویژگی مناسب، تنها داده‌های آموزشی را حفظ می‌کند و قادر به تعمیم الگوی باخت نیست.

---

> **نکته اجرایی:** تمام نوت‌بوک‌های این پوشه در محیط آناکوندا/پایتون۳ قابل اجرا و دارای سلول‌های تست‌شده، جداول عددی و نمودارهای وضوح بالا هستند.

</div>
