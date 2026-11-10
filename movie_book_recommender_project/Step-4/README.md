<div dir="rtl" align="right">

# 📊 گزارش تخصصی گام چهارم: طراحی معماری مدل، انتخاب Baseline و استراتژی ارزیابی
### 📚 سامانه هوشمند پیشنهاددهنده فیلم و کتاب (Cross-Domain Recommender System)

**مسئول بخش طراحی سیستم و معماری مدل:** ابراهیم یدالهی  
**درس:** آزمایشگاه هوش مصنوعی  
**فاز توسعه:** گام چهارم (Step-4: Baseline & Initial Evaluation)  

---

## 🎯 ۱. مقدمه و نقش در گام چهارم

در فاز چهارم پروژه، با توجه به تفکیک مسئولیت‌های فنی و بر اساس ساختار ارائه‌شده در آزمایشگاه هوش مصنوعی، نقش اینجانب **طراح سیستم و معمار مدل (System & Model Designer)** بوده است. وظیفه محوری در این بخش شامل تدوین سند معماری (`DESIGN.md`)، انتخاب و فرمولاسیون ریاضی مدل‌های پایه (Baselines)، گزینش معیارهای استاندارد ارزیابی عملکرد و تعریف پروتکل اعتبارسنجی بدون نشت داده بوده است تا تیم پیاده‌سازی و ارزیابی بر مبنای یک چارچوب مهندسی دقیق عمل کنند.

---

## 🛠️ ۲. شرح اقدامات و وظایف تخصصی انجام‌شده (ابراهیم یدالهی)

- 🔹 **مهار تله دقت و انتخاب خط مبنای عملکرد (Accuracy Trap Mitigation):**
  - تحلیل ریسک تکیه صِرف بر معیارهای ساده در داده‌های نامتوازن و تبیین لزوم ارزیابی چندمعیاره.
  - طراحی سه سطح مدل پایه برای ایجاد کف عملکرد (Lower Bound Benchmark):
    1. **مدل پایه میانگین سراسری (Global Mean):** برای سنجش بدترین سناریوی خطای پیوسته.
    2. **مدل پایه انحرافات کاربر و آیتم (User-Item Baseline Predictor):** مدل‌سازی خطی با منظم‌سازی $L_2$ جهت خنثی‌سازی اثر سخت‌گیری کاربر و محبوبیت کتاب.
    3. **مدل پایه رتبه‌بندی مبتنی بر محبوبیت (Popularity-Based Top-K):** پوشش چالش شروع سرد (Cold-Start) برای کاربران تازه‌وارد.

- 🔹 **انتخاب و فرمولاسیون معیارهای ارزیابی آفلاین (Metric Formulation):**
  - فرموله‌سازی ریاضی معیارهای خطای رگرسیونی پیش‌بینی نمره: **RMSE** و **MAE**.
  - فرموله‌سازی معیارهای سنجش کیفیت فهرست‌های پیشنهادی: **Precision@K**، **Recall@K** و **NDCG@K**.

- 🔹 **طراحی پروتکل ممیزی داده و جلوگیری از نشت اطلاعات (Data Leakage Firewall):**
  - تدوین پروتکل تقسیم قطعی ۸۰٪ آموزش (`Train`) و ۲۰٪ آزمون (`Test`) با تثبیت بذر تصادفی (`random_state=42`).
  - تدوین شرط ریاضی عدم تداخل داده‌های آزمون در استخراج آماره‌های مدل‌سازی: $R_{train} \cap R_{test} = \emptyset$.

- 🔹 **تدوین و نهایی‌سازی سند جامع معماری (`DESIGN.md`):**
  - مستندسازی کامل روابط ریاضی، ماتریس اهداف عملکردی الگوریتم‌ها و جداول استنتاج مهندسی در ساختار استاندارد آزمایشگاه.

---

## 📐 ۳. خلاصه فرمولاسیون مدل‌های پایه طراحی‌شده

### ۱. مدل پایه میانگین سراسری (Global Mean)
$$\hat{r}_{u,i} = \mu = \frac{1}{\vert{}R_{train}\vert{}} \sum_{(u', i') \in R_{train}} r_{u', i'}$$

### ۲. مدل پایه انحرافات خطی با منظم‌سازی (Baseline Predictor with Biases)
$$\hat{r}_{u,i} = \mu + b_u + b_i$$

$$b_u = \frac{\sum_{i \in I_u} (r_{u,i} - \mu)}{\lambda_1 + \vert{}I_u\vert{}}, \quad b_i = \frac{\sum_{u \in U_i} (r_{u,i} - \mu - b_u)}{\lambda_2 + \vert{}U_i\vert{}}$$

---

## 📊 ۴. ماتریس هدف‌گذاری مقایسه مدل‌ها در گام چهارم

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">نوع مدل</th>
      <th style="text-align: right;">نام مدل / الگوریتم</th>
      <th style="text-align: right;">شاخص RMSE (هدف)</th>
      <th style="text-align: right;">شاخص MAE (هدف)</th>
      <th style="text-align: right;">Precision@10</th>
      <th style="text-align: right;">Recall@10</th>
      <th style="text-align: right;">وضعیت در گام چهارم</th>
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
      <td style="text-align: right;">طراحی و فرمول‌بندی شد</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>Baseline 1</b></td>
      <td style="text-align: right;">User-Item Biases</td>
      <td style="text-align: right;">< ۱.۱۵</td>
      <td style="text-align: right;">< ۰.۸۵</td>
      <td style="text-align: right;">۰.۱۲</td>
      <td style="text-align: right;">۰.۰۸</td>
      <td style="text-align: right;">طراحی و فرمول‌بندی شد</td>
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
      <td style="text-align: right;">تحویل به بخش پیاده‌سازی</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>Collaborative</b></td>
      <td style="text-align: right;">Item-Based k-NN</td>
      <td style="text-align: right;">< ۰.۹۴</td>
      <td style="text-align: right;">< ۰.۶۹</td>
      <td style="text-align: right;">> ۰.۲۶</td>
      <td style="text-align: right;">> ۰.۱۹</td>
      <td style="text-align: right;">تحویل به بخش پیاده‌سازی</td>
    </tr>
  </tbody>
</table>

---

## 💡 ۵. تصمیمات مهندسی اتخاذشده در فاز طراحی

<table dir="rtl" style="width: 100%; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right;">مشاهده تحلیلی (Observation)</th>
      <th style="text-align: right;">ریشه آماری (Reason)</th>
      <th style="text-align: right;">تصمیم مهندسی طراح (Conclusion)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right;"><b>چولگی مثبت شدید در توزیع نمرات</b></td>
      <td style="text-align: right;">کاربران عمدتاً آثاری را امتیازدهی می‌کنند که از آن رضایت داشته‌اند.</td>
      <td style="text-align: right;">الزام استفاده از مرکززدایی میانگین کاربر (<code>Mean-Centering</code>) در پیش‌بینی نمرات.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>توزیع دم‌بلند تعاملات اقلام</b></td>
      <td style="text-align: right;">تعداد معدودی از عناوین، بخش اعظم بازخوردها را دریافت کرده‌اند.</td>
      <td style="text-align: right;">افزودن پارامتر منقبض‌کننده $\lambda_2$ در محاسبه انحراف کتاب‌ها برای کنترل اقلام کم‌تعامل.</td>
    </tr>
    <tr>
      <td style="text-align: right;"><b>ناکافی بودن معیار Accuracy</b></td>
      <td style="text-align: right;">نرخ عدم تعادل بالا بین کلاس‌های بازخورد صریح.</td>
      <td style="text-align: right;">به‌کارگیری توأمان معیارهای RMSE، Recall@K و NDCG@K در ارزیابی سیستم.</td>
    </tr>
  </tbody>
</table>

---

## 📂 ۶. ساختار فایل‌های تحویل‌شده در این گام

```text
movie_book_recommender_project/Step-4/
│
├── DESIGN.md       # سند جامع معماری، فرمولاسیون ریاضی و استراتژی ارزیابی (تولیدشده توسط طراح)
└── README.md       # گزارش تخصصی نقش طراحی و هدایت متدولوژی گام چهارم
```

</div>
