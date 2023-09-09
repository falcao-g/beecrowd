SELECT d.name, 
ROUND(SUM((att.hours * 150.0) + (((att.hours * 150.0) * ws.bonus) / 100.0)), 1) AS salary
FROM doctors AS d
INNER JOIN attendances AS att on att.id_doctor = d.id
INNER JOIN work_shifts AS ws on ws.id = att.id_work_shift
GROUP BY d.id
ORDER BY salary DESC