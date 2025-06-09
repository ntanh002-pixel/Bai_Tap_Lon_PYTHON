# file_handler.py

def open_file(filename):
    """
    Đọc file văn bản chứa câu hỏi.
    Mỗi câu hỏi gồm 5 dòng:
    - dòng 1: câu hỏi
    - dòng 2–4: 3 đáp án
    - dòng 5: số thứ tự đáp án đúng (1–3)
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]
            questions = []
            i = 0
            while i + 4 < len(lines):
                question = lines[i]
                answers = lines[i+1:i+4]
                correct_index = int(lines[i+4])  # 1-based index
                if not 1 <= correct_index <= 3:
                    raise ValueError("Đáp án đúng phải là số 1-3.")
                questions.append((question, answers, correct_index))
                i += 5
            return questions
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file: {filename}")
    except Exception as e:
        raise Exception(f"Lỗi khi đọc file: {e}")
