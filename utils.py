import time
 
 
def delay(i=0, n=6):
    for _ in range(n):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n"*i)
    time.sleep(0.6)



def view_records(info):
    print("\nYour Records")
    for year in info.keys():
        for sem in info[year]:
            print(f"\n{" ".join(year.split("_")).title()}, {"ester ".join(sem.split("_")).title()}")

            for det in info[year][sem]:
                print(det["name"], end=" | ")
                print(f"Credit hours: {det["credits"]}", end=" | ")
                print(f"Grade: {det["grades"]}")
    
        