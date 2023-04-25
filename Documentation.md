>Warning

-This is an incomplete program<br/>
*The old UI.py will not be updated and it is only for history<br/><br/>
>Prerequist

```pip install tk```<br/>
```pip install customtkinter```<br/><br/>

>Homework Class

I.Every homework is treated as an homework object under the homework class<br/><br/>

>Adding New Course/Homework To The Database

Example(Adding ELEC2100 HW1, required 130 minutes)<br />
Step 1: (Add the new course if it has not been added)<br/>
```
In Database.py:
course_list.append("ELEC2100")
```

Step2: (Add the new homework)
```
In Database.py:
ELEC2100_HW1 = Homework("ELEC2100", "HW1", 130)
homework_list.append(ELEC2100_HW1)
```
