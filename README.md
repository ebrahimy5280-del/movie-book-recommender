<div dir="rtl" align="right">

# سیستم هوشمند پیشنهاددهنده فیلم و کتاب
### Movie & Book Recommender Agent — آزمایشگاه هوش مصنوعی

**تهیه کننده:** ابراهیم یدالهی  
**درس:** آزمایشگاه هوش مصنوعی | **مراحل:** گام اول (تحلیل مسئله و عامل‌ها) و گام دوم (ساخت داده، ماتریس تعاملات و تفکیک ارزیابی)

این پروژه با هدف طراحی و پیاده‌سازی یک عامل هوشمند برای تحلیل علایق ترکیبی کاربران و ارائه پیشنهادهای شخصی‌سازی‌شده در دو بستر فیلم و کتاب، در قالب گام‌های پروژه آزمایشگاه هوش مصنوعی توسعه داده می‌شود.

---

## ۱. تحلیل مؤلفه‌های PEAS (گام اول)

<table dir="rtl" width="100%">
  <thead>
    <tr>
      <th align="center" width="20%">مؤلفه</th>
      <th align="center" width="20%">عنوان لاتین</th>
      <th align="right" width="60%">شرح در سیستم پیشنهاددهنده فیلم و کتاب</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><b>معیار عملکرد</b></td>
      <td align="center">Performance</td>
      <td>دقت و پوشش اقلام پیشنهادی (Precision / Recall)، کاهش خطای تخمین امتیاز (RMSE)، نرخ تعامل کاربر و تنوع پیشنهادها.</td>
    </tr>
    <tr>
      <td align="center"><b>محیط مسئله</b></td>
      <td align="center">Environment</td>
      <td>پایگاه داده عناوین فیلم‌ها و کتاب‌ها (ژانر، نویسنده/کارگردان)، مشخصات کاربران و تاریخچه امتیازها و تعاملات پیشین.</td>
    </tr>
    <tr>
      <td align="center"><b>عملگرها</b></td>
      <td align="center">Actuators</td>
      <td>رابط کاربری جهت نمایش فهرست مرتب‌شده و رتبه‌بندی‌شده فیلم‌ها و کتاب‌های پیشنهادی و به‌روزرسانی چیدمان صفحه.</td>
    </tr>
    <tr>
      <td align="center"><b>حسگرها</b></td>
      <td align="center">Sensors</td>
      <td>ورودی‌های کاربر شامل امتیازهای ثبت‌شده (۱ تا ۵)، تاریخچه جستجو، لیست علاقه‌مندی‌ها و تعاملات کلیکی.</td>
    </tr>
  </tbody>
</table>

<br>

---

## ۲. مشخصات محیط مسئله (Task Environment Properties)

<table dir="rtl" width="100%">
  <thead>
    <tr>
      <th align="center" width="20%">ویژگی محیط</th>
      <th align="center" width="25%">وضعیت</th>
      <th align="right" width="55%">تحلیل و دلیل</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><b>مشاهده‌پذیری</b></td>
      <td align="center">تا حدی مشاهده‌پذیر<br>(Partially Observable)</td>
      <td>عامل فقط به داده‌های تعاملی ثبت‌شده دسترسی دارد و از حالات روحی لحظه‌ای یا علایق خارج از سیستم مطلع نیست (ماتریس متخلخل).</td>
    </tr>
    <tr>
      <td align="center"><b>تعداد عامل‌ها</b></td>
      <td align="center">تک‌عاملی<br>(Single Agent)
