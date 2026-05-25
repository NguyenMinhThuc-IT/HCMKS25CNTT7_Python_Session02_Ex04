print("===== HỆ THỐNG SÀNG LỌC TIỀN PHẪU THUẬT =====")

try:
    patient_age = int(input(
        "Nhập tuổi bệnh nhân (Ví dụ: 45): "
    ))

    systolic_blood_pressure = int(input(
        "Nhập huyết áp tâm thu mmHg (Ví dụ: 120): "
    ))

    blood_sugar = int(input(
        "Nhập đường huyết mg/dL (Ví dụ: 110): "
    ))

    if (
        patient_age < 0
        or systolic_blood_pressure < 0
        or blood_sugar < 0
    ):
        print("Dữ liệu nhập vào không hợp lệ")

    else:

        if patient_age < 75:

            if 90 <= systolic_blood_pressure <= 140:

                if blood_sugar < 150:

                    print("\n===== KẾT QUẢ =====")
                    print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")

                else:

                    print("\n===== KẾT QUẢ =====")
                    print("TỪ CHỐI PHẪU THUẬT")
                    print("Lý do: Đường huyết vượt ngưỡng an toàn")

            else:

                print("\n===== KẾT QUẢ =====")
                print("TỪ CHỐI PHẪU THUẬT")
                print("Lý do: Huyết áp tâm thu ngoài giới hạn 90 - 140 mmHg")

        else:

            print("\n===== KẾT QUẢ =====")
            print("TỪ CHỐI PHẪU THUẬT")
            print("Lý do: Tuổi bệnh nhân phải dưới 75")

except ValueError:

    print("Dữ liệu nhập vào không hợp lệ")
