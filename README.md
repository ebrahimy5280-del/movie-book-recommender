<div dir="rtl" align="right">

# سیستم هوشمند پیشنهاددهنده فیلم و کتاب
### Movie & Book Recommender Agent — آزمایشگاه هوش مصنوعی

این مخزن مربوط به پیاده‌سازی گام اول پروژه درس آزمایشگاه هوش مصنوعی است. هدف پروژه، تحلیل مسئله، تعریف عامل هوشمند پیشنهاددهنده و شبیه‌سازی رفتار عامل‌ها در ارائه پیشنهادات شخصی‌سازی‌شده فیلم و کتاب به کاربران می‌باشد.

---

## ۱. تحلیل مؤلفه‌های چهارگانه مسئله (PEAS)

<table dir="rtl" align="right">
  <thead>
    <tr>
      <th align="center" width="22%">مؤلفه</th>
      <th align="center" width="18%">عنوان لاتین</th>
      <th align="right" width="60%">شرح در سیستم پیشنهاددهنده فیلم و کتاب</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><b>معیار عملکرد</b></td>
      <td align="center"><code dir="ltr">Performance</code></td>
      <td>دقت و پوشش اقلام پیشنهادی (<code dir="ltr">Precision / Recall</code>)، کاهش خطای تخمین امتیاز (<code dir="ltr">RMSE</code>)، نرخ کلیک کاربر روی پیشنهادات و تنوع ژانری اقلام.</td>
    </tr>
    <tr>
      <td align="center"><b>محیط مسئله</b></td>
      <td align="center"><code dir="ltr">Environment</code></td>
      <td>بانک اطلاعاتی فیلم‌ها و کتاب‌ها (شامل ژانر، سال، نویسنده/کارگردان)، پایگاه داده کاربران، تاریخچه امتیازدهی‌ها و تعاملات پیشین.</td>
    </tr>
    <tr>
      <td align="center"><b>عملگرها</b></td>
      <td align="center"><code dir="ltr">Actuators</code></td>
      <td>رابط کاربری جهت نمایش لیست مرتب‌شده پیشنهادها، فیلتر کردن عناوین و به‌روزرسانی چیدمان صفحه اصلی کاربر.</td>
    </tr>
    <tr>
      <td align="center"><b>حسگرها</b></td>
      <td align="center"><code dir="ltr">Sensors</code></td>
      <td>ورودی‌های دریافتی از کاربر شامل امتیازهای ثبت‌شده (۱ تا ۵ ستاره)، جستجوها، لیست علاقه‌مندی‌ها و رفتارهای کلیکی.</td>
    </tr>
  </tbody>
</table>

<br>

---

## ۲. مشخصات محیط مسئله (Task Environment Properties)

شش ویژگی بنیادین محیط مسئله بر اساس دسته‌بندی استاندارد هوش مصنوعی:

<table dir="rtl" align="right">
  <thead>
    <tr>
      <th align="center" width="20%">ویژگی محیط</th>
      <th align="center" width="25%">وضعیت در سیستم</th>
      <th align="right" width="55%">تحلیل و دلیل</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><b>مشاهده‌پذیری</b></td>
      <td align="center">تا حدی مشاهده‌پذیر<br><code dir="ltr">(Partially Observable)</code></td>
      <td>عامل تنها به داده‌های ثبت‌شده داخل پلتفرم دسترسی دارد و از حالات روحی لحظه‌ای، تجربیات بیرونی یا علایق ناگفته کاربر بی‌خبر است.</td>
    </tr>
    <tr>
      <td align="center"><b>تعداد عامل‌ها</b></td>
      <td align="center">تک‌عاملی<br><code dir="ltr">(Single Agent)</code></td>
      <td>عامل پیشنهاددهنده به تنهایی داده‌ها را پردازش کرده و رتبه‌بندی اقلام را انجام می‌دهد؛ عامل یا رقیب دیگری برای تداخل عملکرد وجود ندارد.</td>
    </tr>
    <tr>
      <td align="center"><b>قطعیت</b></td>
      <td align="center">احتمالاتی / تصادفی<br><code dir="ltr">(Stochastic)</code></td>
      <td>رفتار کاربر و بازخورد او به یک پیشنهاد با قطعیت قابل پیش‌بینی نیست و یک آیتم یکسان ممکن است در زمان‌های مختلف واکنش متفاوتی ایجاد کند.</td>
    </tr>
    <tr>
      <td align="center"><b>مرحله‌ای بودن</b></td>
      <td align="center">ترتیبی<br><code dir="ltr">(Sequential)</code></td>
      <td>پیشنهادات فعلی روی سلیقه و تاریخچه کاربر اثر می‌گذارد و تعاملات گذشته مستقیماً بر پیشنهادهای گام‌های بعدی تأثیرگذار خواهند بود.</td>
    </tr>
    <tr>
      <td align="center"><b>پویایی</b></td>
      <td align="center">پویا<br><code dir="ltr">(Dynamic)</code></td>
      <td>محیط با گذشت زمان تغییر می‌کند؛ کاتالوگ فیلم‌ها و کتاب‌های جدید اضافه می‌شوند و سلیقه کاربر نیز به مرور زمان دستخوش تغییر می‌گردد.</td>
    </tr>
    <tr>
      <td align="center"><b>پیوستگی</b></td>
      <td align="center">گسسته<br><code dir="ltr">(Discrete)</code></td>
      <td>مجموعه فیلم‌ها، کتاب‌ها، رتبه‌ها و امتیازهای دریافتی (مانند امتیازهای گسسته ۱ تا ۵) دارای مقادیر و دسته‌بندی‌های مشخص و متناهی هستند.</td>
    </tr>
  </tbody>
</table>

<br>

---

## ۳. ساختار فایل‌های مخزن

* `README.md`: تحلیل کامل PEAS و ویژگی‌های ۶ گانه محیط مسئله.
* `notes/risks.md`: مستندسازی معیارهای ارزیابی (<code dir="ltr">Precision, Recall, NDCG, RMSE</code>) و بررسی ریسک‌های اصلی سامانه.
* `check_env.ipynb`: نوت‌بوک اعتبارسنجی محیط توسعه شامل نسخه پایتون، مسیر اجرایی و پکیج‌های پایه.
* `recommender_agent.py`: شبیه‌سازی و مقایسه عملکرد ۳ معماری عامل (<code dir="ltr">Random, Reflex, Model-based</code>) در بستر پیشنهاد فیلم و کتاب.
* `requirements.txt`: فهرست کتابخانه‌های پایتون مورد نیاز برای اجرای پروژه.

---

## ۴. نحوه اجرای شبیه‌سازی عامل‌ها

جهت اجرای اسکریپت مقایسه عامل‌ها و رسم نمودار ارزیابی، دستور زیر را در ترمینال اجرا کنید:

```bash
pip install -r requirements.txt
python recommender_agent.py
