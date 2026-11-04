<div dir="rtl">

# 📚 تمرین‌ها و تکالیف هفتگی آزمایشگاه هوش مصنوعی

**تهیه‌کننده: ابراهیم یدالهی**  
**درس:** آزمایشگاه هوش مصنوعی  
**محیط اجرا:** پایتون ۳.۱۴، Conda (`ailab`) و نوت‌بوک تعاملی ژوپیتر

این پوشه شامل تمرین‌های عملی، فعالیت‌های کلاسی و نوت‌بوک‌های تحلیلی هر جلسه از درس آزمایشگاه هوش مصنوعی است. ساختار و شرح تمرین‌ها به تفکیک جلسات به شرح زیر است:

---

## 🗓 فهرست جلسات و فایل‌ها

### ۱. جلسه اول: آماده‌سازی و بررسی محیط توسعه
- **فایل:** `check_env.ipynb`
- **شرح مختصر:** راه‌اندازی و اعتبارسنجی محیط توسعه کلاسی پایتون و ابزارهای موردنیاز، شامل تست و بررسی نصب بودن صحیح کتابخانه‌های اصلی پردازش داده و یادگیری ماشین (مانند `numpy`، `pandas`، `matplotlib` و `scipy`).

---

### ۲. جلسه دوم و سوم: پیاده‌سازی و مقایسه الگوریتم‌های جستجو و مسیریابی
- **فایل:** `lab2_pathfinding.ipynb`
- **شرح مختصر:** پیاده‌سازی مسئله حرکت عامل (ربات) در محیط مشبک دوبعدی (Grid) با موانع تصادفی، مقایسه جامع عملکرد الگوریتم‌های جستجوی ناآگاهانه (`BFS` و `DFS`) با الگوریتم آگاهانه (`A*` بر پایه هیوریستیک منهتن) در ۱۰۰ نقشه مختلف، به همراه پاسخ کامل به سوالات تحلیلی رفتار الگوریتم‌ها و پیاده‌سازی چالش حرکت ۸ جهته با هیوریستیک چبیشف.

---

### ۳. جلسه چهارم: بازی Nim با جستجوی تقابلی (Minimax و هرس Alpha-Beta) و تحلیل EDA
- **فایل:** `lab3_nim_minimax_eda_graphical.ipynb`
- **شرح مختصر:** مدل‌سازی بازی ریاضی نیم (Nim) با دو بازیکن A (بیشینه‌ساز / MAX) و B (کمینه‌ساز / MIN) در قالب جستجوی تقابلی و مجموع صفر. پیاده‌سازی و مقایسه گره‌های پیمایش‌شده الگوریتم Minimax در برابر هرس آلفا-بتا (با ترتیب پیش‌فرض و بهینه `big_first`)، تولید پایگاه داده ۲۰۰ بازی شبیه‌سازی‌شده و ممیزی کیفیت داده‌ها، رسم گرید ۴ نمودار تحلیلی، پیاده‌سازی رابط کاربری تعاملی انسان در برابر هوش مصنوعی با ابزارک‌های `ipywidgets` و اجرای چالش تکمیلی قانون معکوس (Misère Nim Rule).

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
  </tbody>
</table>

---

## 🔬 جزئیات و برون‌دادهای تحلیلی تمرین جلسه چهارم (بازی Nim)

### ۱. مقایسه هزینه محاسباتی الگوریتم‌های جستجو
برای پشته کلاسیک شروع `(3, 4, 5)`، تعداد گره‌های پیمایش‌شده به شرح زیر ارزیابی گردید:
* **الگوریتم Minimax کامل:** بررسی **۱٬۰۳۸٬۷۶۸ گره** (بررسی تمامی انشعاب‌های درخت بازی)
* **الگوریتم Alpha-Beta (ترتیب پیش‌فرض):** بررسی **۳۳٬۹۱۶ گره**
* **الگوریتم Alpha-Beta (ترتیب بهینه `big_first`):** بررسی **۴٬۳۳۲ گره** (کاهش بیش از ۹۹.۵ درصدی محاسبات نسبت به مینی‌مکس)

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

### ۳. چالش توسعه‌یافته (Extension Challenge): قانون معکوس (Misère Play)
در انتهای نوت‌بوک، تابع `minimax_misere` پیاده‌سازی گردید که در آن شرط پایان معکوس شده است؛ بازیکنی که آخرین سنگ را بردارد بازنده اعلام می‌شود. با اجرای این تابع برای حالت شروع `(1, 2, 3)`، خروجی مقدار `-1` به دست آمد که نشان می‌دهد بازیکن دوم (B) در بازی معکوس برنده است.

---

> **نکته اجرایی:** تمام نوت‌بوک‌های این پوشه در محیط آناکوندا/پایتون۳ قابل اجرا و دارای خروجی‌ها، جداول و گرافیک‌های اعتبارسنجی‌شده هستند.

</div>
