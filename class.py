class person:
    def __init__(me, kings, rule):
        me.kings=kings
        me.rule=rule
    def display(me):
        print("kings:"+me.kings )
        print(f"rule:{me.rule}")
c1=person("rama",35)
c1.display()

