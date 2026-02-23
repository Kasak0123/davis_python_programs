def attendance_tracker(attendance_records):
    results = []
    
    for idx, record in enumerate(attendance_records, start=1):
        # Step 1: Calculate percentage
        percentage = (sum(record) / len(record)) * 100
        
        # Step 2: Identify below 75%
        status = "OK" if percentage >= 75 else "Below 75%"
        
        # Step 3: Replace consecutive absences with warning
        flagged_record = []
        i = 0
        while i < len(record):
            if record[i] == 0:
                # check consecutive absences
                count = 1
                while i+count < len(record) and record[i+count] == 0:
                    count += 1
                if count > 1:
                    flagged_record.append("W")  # warning flag
                    i += count
                    continue
            flagged_record.append(record[i])
            i += 1
        
        results.append({
            "Student": idx,
            "Attendance %": round(percentage, 2),
            "Status": status,
            "Flagged Record": flagged_record
        })
    
    # Display results
    for res in results:
        print(res)


# Example usage
attendance_data = [
    [1,0,1,1,0,0,1],   # Student 1
    [1,1,1,1,1,1,1],   # Student 2
    [0,0,1,0,1,0,1]    # Student 3
]

attendance_tracker(attendance_data)