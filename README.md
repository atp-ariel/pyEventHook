<div align="center">
    <h1>pyEventHook</h1>
</div>

A Python event implementation similar to the C# implementation.

## Examples

Create an event and suscribe handlers.

```
def wake_up(name):
    print(f"Wake up, {name}!")

def eat_breakfast(name):
    print(f"{name}, remember take your breakfast.")

morning_time = Event()

morning_time += wake_up
morning_time += eat_breakfast

morning_time("Ariel")

# Output
# >> Wake up, Ariel!
# >> Ariel, remember take your breakfast.
```

Unsuscribe from event

```
def wake_up(name):
    print(f"Wake up, {name}!")

def eat_breakfast(name):
    print(f"{name}, remember take your breakfast.")

morning_time = Event()

morning_time += wake_up
morning_time += eat_breakfast

morning_time("Ariel")

morning_time -= wake_up

morning_time("Ariel")

# Output
# >> Wake up, Ariel!
# >> Ariel, remember take your breakfast.
# >> Ariel, remember take your breakfast.
```
