<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <style>
        /* ضع هنا تنسيقات الـ CSS السابقة (الخلفية الداكنة، الرصيد، الأيقونات) */
    </style>
</head>
<body>

    <div class="dashboard">
        </div>

    <script>
        // وظيفة الإرسال المعدلة لتتصل بالسيرفر الخاص بك
        async function sendOrderToBot() {
            const orderData = {
                type: "طلب رشق",
                details: {
                    "المنصة": document.getElementById('platform').value,
                    "الخدمة": document.getElementById('serviceType').value,
                    "الرابط": document.getElementById('targetLink').value,
                    "الكمية": document.getElementById('quantity').value,
                    "السعر": document.getElementById('totalPrice').innerText + "$"
                }
            };

            try {
                const response = await fetch('http://localhost:3000/api/send-order', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(orderData)
                });
                
                if (response.ok) alert("تم إرسال الطلب للسيرفر بنجاح!");
            } catch (error) {
                alert("خطأ في الاتصال بالسيرفر");
            }
        }
    </script>
</body>
</html>
