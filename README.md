# سیستم اداری
ابتدا باید ERD  یک سیستم اداری شامل سیستم های مالی ، سیستم ورود و خروج کارمندان ، که شامل ثبت ورود و خروج کارمندان است و همچنین سیستم مربوط به اطلاعات کارمندان که اطلاعات آن ها درون این سیستم ثبت شده و همچنین امور تغذیه و محاسبه ی مرخصی و تاخیر افراد و به طور کلی محاسبه ی حقوق افراد با درنظر گرفتن بیمه و مزایا و وام وتمام هرینه های جانبی دیگر را میکشیم و سپس نموار فیزیکی و منطقی آن را میکشیم. 

سپس اسکریپت آن را در دیتابیس اوراکل مینویسیم و در نهایت جداوی را که در طراحی نمودار کشیدیم را در دیتابیس ایجاد میکنیم .

در گام بعدی قصد ایجاد فرم برای ثبت اطلاعات در دیتابیس و تعامل با جداول را داریم که به این منظور از زبان پایتون استفاده میکنیم . ابتدا باید کد پایتون را به اوراکل متصل کنیم که برای این کار ابتدا کتابخانه Oracledb را اضافه میکنیم.و سپس  instant client oracle  را نصب کرده و آدرس آن را به تابع init_oracle_client  میدهیم  و پس از وارد کردن اطلاعات 
یوزرنیم و پسورد به دیتابیس متصل میشویم.

بعداز اتصال به دیتابیس شروع به نوشتن کد میکنیم. ابن برنامه شامل 3 فرم گرفتن اطلاعات کارمندان ، ثبت ورود و خروج و در نهایت محاسبه حقوق ماهانه و نمایش فیش حقوقی میباشد.

برای پیاده سازی این فرم ها از کتابخانه ی tkinter استفاده میکنیم.


