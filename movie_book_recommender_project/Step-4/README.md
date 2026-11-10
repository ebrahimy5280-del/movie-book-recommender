<div dir="rtl" align="right">

# 📊 گزارش تخصصی و تفصیلی گام چهارم: مهندسی معماری، تدوین مدل‌های پایه و استراتژی اعتبارسنجی
### 📚 سامانه هوشمند پیشنهاددهنده فیلم و کتاب (Cross-Domain Recommender System)

**مسئول بخش طراحی سیستم و معماری مدل:** ابراهیم یدالهی  
**درس:** آزمایشگاه هوش مصنوعی  
**فاز توسعه:** گام چهارم (Step-4: Baseline & Initial Evaluation)  

---

## 🎯 ۱. مقدمه، تشریح نقش و اهداف بنیادین گام چهارم

در فاز چهارم از چرخه توسعه پروژه سیستم پیشنهاددهنده هوشمند، با استناد به مدل تقسیم کار تخصصی ارائه‌شده در آزمایشگاه هوش مصنوعی، مسئولیت اینجانب به عنوان **طراح سیستم و معمار مدل (System & Model Designer)** تعریف شده است. 

در این گام، هدف اصلی ایجاد یک چارچوب تئوری، ریاضی و ساختاریافته برای مقایسه مدل‌ها و مهار مخاطرات رایج یادگیری ماشین است:
- **جلوگیری از پدیده تله دقت (Accuracy Trap):** در ماتریس‌های تنک و نامتوازن، پیش‌بینی یکنواخت کلاس اکثریت یا مقدار ثابت می‌تواند دقت ظاهری بالایی تولید کند در حالی که مدل هیچ الگوی تعاملی مفیدی را استخراج نکرده است.
- **ایجاد کف عملکرد تجربی (Empirical Baseline Benchmark):** طراحی مدل‌های پایه استاندارد تا عملکرد هرگونه الگوریتم یادگیری نظارت‌شده یا مشارکتی بعدی، در مقایسه با این مبناهای ارزیابی اولیه سنجیده شود.
- **تضمین سلامت پایپ‌لاین آزمون (Data Hygiene & Leakage Prevention):** تدوین ضوابط قطعی برای ایزوله‌سازی کامل فاز آزمون از فاز آموزش، جهت پیشگیری از اعتبارسنجی‌های بیش‌ازحد خوش‌بینانه.

---

## 🛠️ ۲. شرح تفصیلی اقدامات و مسئولیت‌های اجرایی (ابراهیم یدالهی)

### ۲.۱. طراحی و فرمولاسیون سلسله‌مراتبی مدل‌های پایه (Baseline Hierarchy)
- **مدل پایه سطح صفر (Global Mean):** محاسبه میانگین سراسری به عنوان ارزان‌ترین تخمین پیوسته با پیچیدگی محاسباتی $O(1)$ در زمان استنتاج، جهت ثبت بدترین سناریوی خطای سیستم.
- **مدل پایه سطح یک (User-Item Bias Predictor):** فرموله‌سازی اثر انحراف فردی کاربر ($b_u$) و محبوبیت اثر محتوایی ($b_i$) نسبت به میانگین کل. به‌کارگیری منظم‌سازی درجه دو ($L_2$ Regularization) جهت منقبض ساختن اثر نمرات پرت در کاربران و اقلام با تاریخچه تعامل محدود.
- **مدل پایه رتبه‌بندی کاتالوگ (Popularity-Based Top-K):** تدوین منطق رتبه‌بندی وزنی بیزی (Bayesian Weighted Rating) برای استخراج محبوب‌ترین اقلام کاتالوگ و پاسخ‌گویی به چالش کاربران فاقد سابقه (User Cold-Start).

### ۲.۲. انتخاب و فرموله‌سازی معیارهای ارزیابی آفلاین (Offline Evaluation Suite)
- **معیارهای خطای پیش‌بینی مقدار نمره (Rating Prediction Metrics):**
  - فرموله‌سازی معیار **RMSE** با جریمه درجه دو برای خطاهای بزرگ، به عنوان شاخص کلیدی مقایسه مدل‌های رگرسیونی نمرات.
  - فرموله‌سازی معیار **MAE** به عنوان خطای مطلق خطی و مقاوم در برابر داده‌های پرت دورافتاده.
- **معیارهای ارزیابی کیفیت فهرست پیشنهادی (Top-K Ranking Metrics):**
  - تبدیل داده‌های تست به تعاملات باینری رضایت بر اساس آستانه کیفی (نمره $\ge 4$ برای فیلم و $\ge 8$ برای کتاب).
  - فرموله‌سازی معیارهای **Precision@K** و **Recall@K** جهت سنجش دقت بازشناسی و پوشش کامل سلایق کاربر.
  - تدوین ساختار معیار **NDCG@K** با لحاظ افت لگاریتمی جایگاه اقلام در فهرست توصیه‌ها.

### ۲.۳. طراحی پروتکل ممیزی داده و فایروال عدم نشت (Data Leakage Firewall)
- تعیین نسبت قطعی ۸۰٪ برای مجموعه آموزش (`Train`) و ۲۰٪ برای مجموعه آزمون (`Test`) با تثبیت بذر تصادفی یکنواخت (`random_state=42`).
- اعمال شرط اعتبارسنجی بدون نشت داده؛ عدم استفاده از اطلاعات، آماره‌ها، مقادیر گمشده و توزیع‌های مجموعه آزمون در زمان استخراج پارامترهای مدل پایه:
  $$R_{train} \cap R_{test} = \emptyset$$

### ۲.۴. نگارش و یکپارچه‌سازی اسناد فنی گام چهارم
- تدوین سند تفصیلی معماری در فایل `DESIGN.md` حاوی توجیه ریاضی، جداول مقایسه و اهداف عملیاتی الگوریتم‌ها.
- تدوین گزارش اختصاصی نقش طراحی در فایل `README.md` جهت شفاف‌سازی مسیر توسعه برای بخش‌های پیاده‌سازی و ارزیابی.

---

## 📐 ۳. روابط ریاضی و فرمولاسیون مدل‌های پایه طراحی‌شده

### ۱. مدل پایه میانگین سراسری (Global Mean Baseline)
$$\hat{r}_{u,i} = \mu = \frac{1}{\vert{}R_{train}\vert{}} \sum_{(u', i') \in R_{train}} r_{u', i'}$$

### ۲. مدل پایه انحرافات خطی کاربر و آیتم با منظم‌سازی (Baseline Predictor with Biases)
$$\hat{r}_{u,i} = \mu + b_u + b_i$$

$$b_u = \frac{\sum_{i \in I_u} (r_{u,i} - \mu)}{\lambda_1 + \vert{}I_u\vert{}}$$

$$b_i = \frac{\sum_{u \in U_i} (r_{u,i} - \mu - b_u)}{\lambda_2 + \vert{}U_i\vert{}}$$

- $\mu$: میانگین نمرات در مجموعه آموزش
- $b_u$: ضریب تمایل یا سخت‌گیری کاربر $u$ نسبت به میانگین سراسری
- $b_i$: ضریب محبوبیت یا عدم اقبال کتاب/فیلم $i$ نسبت به میانگین سراسری
- $\lambda_1, \lambda_2$: پارامترهای تنظیم‌کننده انقباض نمرات برای موجودیت‌های کم‌تعامل

---

## 📊 ۴. ماتریس هدف‌گذاری مقایسه مدل‌ها در گام چهارم

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
      <td style="text-align: right;">طراحی شد (پروتکل شروع سرد)</td>
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

## 💡 ۵. تصمیمات مهندسی اتخاذشده در فاز طراحی معماری

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">مشاهده تحلیلی (Observation)</th>
      <th style="text-align: right;">ریشه آماری و رفتاری (Reason)</th>
      <th style="text-align: right;">تصمیم مهندسی طراح (Conclusion)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>چولگی مثبت شدید در توزیع نمرات</b></td>
      <td style="text-align: right;">کاربران عمدتاً آثاری را تجربه و ثبت امتیاز می‌کنند که از پیش به آن علاقه داشته‌اند (Positive Selection Bias).</td>
      <td style="text-align: right;">الزام استفاده از مرکززدایی میانگین کاربر (<code>Mean-Centering</code>) در فرمولاسیون مدل‌ها جهت هم‌مقیاس‌سازی رفتار کاربران سخت‌گیر و آسان‌گیر.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>توزیع دم‌بلند تعاملات اقلام (Power Law)</b></td>
      <td style="text-align: right;">عناوین شناخته‌شده سهم بزرگی از تعاملات را جذب کرده‌اند در حالی که کاتالوگ وسیعی از کتاب‌ها تعامل بسیار اندکی دارند.</td>
      <td style="text-align: right;">افزودن پارامتر منقبض‌کننده $\lambda_2$ در محاسبه انحراف کتاب‌ها برای کنترل اقلام کم‌تعامل و پیشگیری از تصمیم‌گیری‌های ناپایدار.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>ناکافی بودن شاخص Accuracy</b></td>
      <td style="text-align: right;">عدم تعادل بین بازخوردهای ثبت‌شده و اقلام نادیده‌گرفته‌شده، مفهوم دقت کلی را بی‌اثر و گمراه‌کننده می‌سازد.</td>
      <td style="text-align: right;">به‌کارگیری توأمان معیارهای RMSE برای خطای عددی و Recall@K و NDCG@K برای ارزیابی رتبه‌بندی اقلام مورد علاقه.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>ریسک نشت داده میان ترین و تست</b></td>
      <td style="text-align: right;">تخمین میانگین‌ها یا انحرافات با کل داده‌ها پیش از تفکیک، منجر به نتایج غیرواقعی و بیش‌برازش پنهان می‌شود.</td>
      <td style="text-align: right;">ایجاد پروتکل سخت‌گیرانه فایروال نشت داده و استخراج کلیه پارامترهای آماری صرفاً از زیرمجموعه آموزش.</td>
    </tr>
  </tbody>
</table>

---

## 📂 ۶. ساختار فایل‌های تحویل‌شده در پوشه گام چهارم

```text
movie_book_recommender_project/Step-4/
│
├── DESIGN.md       # سند جامع معماری، فرمولاسیون ریاضی و استراتژی ارزیابی (تولیدشده توسط طراح)
└── README.md       # گزارش تخصصی و تحلیلی نقش طراحی و هدایت متدولوژی گام چهارم
```

</div>
