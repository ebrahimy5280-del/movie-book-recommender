<div dir="rtl" align="right">

# سیستم هوشمند پیشنهاددهنده فیلم و کتاب
### Movie & Book Recommender Agent — آزمایشگاه هوش مصنوعی

این مخزن شامل مستندات و پیاده‌سازی گام اول پروژه درس آزمایشگاه هوش مصنوعی با موضوع طراحی و ارزیابی عامل هوشمند پیشنهاددهنده فیلم و کتاب است. در این گام، ویژگی‌های مسئله مدل‌سازی شده، محیط آزمایشگاهی اعتبارسنجی گردیده و معماری‌های پایه عامل شبیه‌سازی شده‌اند.

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
      <td>دقت و پوشش اقلام پیشنهادی (<code dir="ltr">Precision / Recall</code>)، کاهش خطای تخمین امتیاز (<code dir="ltr">RMSE</code>)، نرخ تعامل کاربر و تنوع ژانری توصیه‌ها.</td>
    </tr>
    <tr>
      <td align="center"><b>محیط مسئله</b></td>
      <td align="center"><code dir="ltr">Environment</code></td>
      <td>پایگاه داده عناوین فیلم‌ها و کتاب‌ها (ژانر، نویسنده/کارگردان)، مشخصات کاربری و تاریخچه امتیازها و تعاملات گذشته.</td>
    </tr>
    <tr>
      <td align="center"><b>عملگرها</b></td>
      <td align="center"><code dir="ltr">Actuators</code></td>
      <td>رابط کاربری سامانه جهت نمایش فهرست رتبه‌بندی‌شده عناوین، اعمال فیلترها و چیدمان پویای بخش پیشنهادات.</td>
    </tr>
    <tr>
      <td align="center"><b>حسگرها</b></td>
      <td align="center"><code dir="ltr">Sensors</code></td>
      <td>سیگنال‌های دریافتی از رفتارهای کاربر شامل امتیازهای عددی ثبت‌شده (۱ تا ۵)، عبارات جستجو، لیست علاقه‌مندی‌ها و تعاملات کلیکی.</td>
    </tr>
  </tbody>
</table>

<br>

---

## ۲. مشخصات محیط مسئله (Task Environment Properties)

تحلیل ویژگی‌های شش‌گانه محیط کاری عامل توصیه‌گر بر مبنای دسته‌بندی مسائل هوش مصنوعی:

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
      <td>عامل تنها به تعاملات ثبت‌شده در سیستم دسترسی دارد و از حالات ذهنی یا اولویت‌های خارج از بستر سامانه کاربر مطلع نیست.</td>
    </tr>
    <tr>
      <td align="center"><b>تعداد عامل‌ها</b></td>
      <td align="center">تک‌عاملی<br><code dir="ltr">(Single Agent)</code></td>
      <td>عامل پیشنهاددهنده بدون حضور عامل رقیب یا همکار، به شکل مستقل وظیفه استخراج الگوها و رتبه‌بندی اقلام را انجام می‌دهد.</td>
    </tr>
    <tr>
      <td align="center"><b>قطعیت</b></td>
      <td align="center">احتمالاتی / تصادفی<br><code dir="ltr">(Stochastic)</code></td>
      <td>عکس‌العمل کاربر به یک توصیه دارای قطعیت کامل نیست و ممکن است در زمان‌های مختلف رفتارهای متفاوتی بروز دهد.</td>
    </tr>
    <tr>
      <td align="center"><b>مرحله‌ای بودن</b></td>
      <td align="center">ترتیبی<br><code dir="ltr">(Sequential)</code></td>
      <td>هر بازخورد کاربر، مدل حافظه و پروفایل او را به‌روزرسانی کرده و مستقیماً کیفیت پیشنهادهای گام‌های بعدی را تعیین می‌کند.</td>
    </tr>
    <tr>
      <td align="center"><b>پویایی</b></td>
      <td align="center">پویا<br><code dir="ltr">(Dynamic)</code></td>
      <td>محیط با ورود کتاب‌ها و فیلم‌های جدید و تغییر پیوسته تمایلات کاربر در گذر زمان تغییر می‌کند.</td>
    </tr>
    <tr>
      <td align="center"><b>پیوستگی</b></td>
      <td align="center">گسسته<br><code dir="ltr">(Discrete)</code></td>
      <td>تعداد عناوین کاتالوگ، دسته‌بندی ژانرها و بازه امتیازدهی کاربران مقادیری مشخص و گسسته هستند.</td>
    </tr>
  </tbody>
</table>

<br>

---

## ۳. ساختار فایل‌های مخزن

<table dir="rtl" align="right">
  <thead>
    <tr>
      <th align="center" width="30%">نام فایل / مسیر</th>
      <th align="right" width="70%">شرح محتوا و هدف</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><code dir="ltr">README.md</code></td>
      <td>مستندسازی مؤلفه‌های PEAS، تحلیل ۶ ویژگی محیط مسئله و راهنمای ساختار کلی مخزن.</td>
    </tr>
    <tr>
      <td align="center"><code dir="ltr">notes/risks.md</code></td>
      <td>تشریح معیارهای ارزیابی کمّی و کیفی همراه با تحلیل ۴ چالش کلیدی و راهکارهای متناظر.</td>
    </tr>
    <tr>
      <td align="center"><code dir="ltr">check_env.ipynb</code></td>
      <td>نوت‌بوک تست صحت محیط اجرایی، مفسر پایتون و نسخه‌های پکیج‌های پایه همراه با خروجی اجرا.</td>
    </tr>
    <tr>
      <td align="center"><code dir="ltr">recommender_agent.py</code></td>
      <td>کد شبیه‌سازی و مقایسه عملکرد ۳ معماری عامل (تصادفی، واکنشی و مبتنی بر مدل) در محیط پیشنهاد کالا.</td>
    </tr>
    <tr>
      <td align="center"><code dir="ltr">requirements.txt</code></td>
      <td>فهرست وابستگی‌ها و پکیج‌های مورد نیاز جهت بازتولید آزمایش‌ها.</td>
    </tr>
  </tbody>
</table>

<br>

---

## ۴. نحوه اجرای شبیه‌سازی

جهت نصب پیش‌نیازها، اجرای شبیه‌سازی و مشاهده مقایسه عملکرد عامل‌ها:

```bash
pip install -r requirements.txt
python recommender_agent.py
