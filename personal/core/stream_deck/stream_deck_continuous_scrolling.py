from talon import ui, Module, Context, registry, actions, imgui, cron, app, scope
mod = Module()
ctx_continuous_scrolling = Context()
ctx_continuous_scrolling.matches = r"""
tag: user.continuous_scrolling
"""

@ctx_continuous_scrolling.action_class("user")
class ContinuousScrollingActions:
    def deck1():
        """document string goes here"""
        pass
        
        actions.deck.goto("A00SA3192M9DW0", "default")
        

    def deck2():
        """document string goes here"""
        pass


    def deck3():
        """document string goes here"""
        actions.user.mouse_scroll_down_continuous()
        if not actions.user.mouse_is_continuous_scrolling():
            actions.deck.goto("A00SA3192M9DW0", "default")



    def deck4():
        """document string goes here"""
        actions.user.mouse_scroll_up_continuous()
        if not actions.user.mouse_is_continuous_scrolling():
            actions.deck.goto("A00SA3192M9DW0", "default")



    def deck5():
        """document string goes here"""
        actions.user.mouse_scroll_set_speed(5)



    def deck6():
        """document string goes here"""
        actions.user.mouse_scroll_set_speed(10)

    def deck7():
        """document"""
        actions.user.mouse_scroll_set_speed(25)
    
    def deck8():
        actions.user.mouse_scroll_set_speed(35)
    
    def deck9():
        actions.user.mouse_scroll_set_speed(55)

    def deck10():
        actions.user.mouse_scroll_set_speed(100)
    
    def deck11():
        actions.deck.goto("A00SA3192M9DW0", "default")

    def deck12():
        actions.deck.goto("A00SA3192M9DW0", "default")
