from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/Arch/scripts/autostart.sh')
    subprocess.Popen([home])

mod = "mod4"

keys = [
    Key([mod], "left", lazy.layout.left()),
    Key([mod], "right", lazy.layout.right()),
    Key([mod], "down", lazy.layout.down()),
    Key([mod], "up", lazy.layout.up()),
    
    Key([mod, "shift"], "left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up()),
    
    Key([mod, "control"], "left", lazy.layout.grow_left()),
    Key([mod, "control"], "right", lazy.layout.grow_right()),
    Key([mod, "control"], "down", lazy.layout.grow_down()),
    Key([mod, "control"], "up", lazy.layout.grow_up()),

    Key([mod], "space", lazy.layout.normalize()),
    Key([mod], "w", lazy.window.kill()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "control"], "f", lazy.window.toggle_floating()),

    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),

    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "r", lazy.spawn("rofi -show drun -icon-theme 'Papirus' -show-icons ")),
    Key([mod], "e", lazy.spawn("thunar")),

    Key([], "XF86AudioRaiseVolume", lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ +5%')),
    Key([], "XF86AudioLowerVolume", lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ -5%')),
    Key([], "XF86AudioMute", lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle')),

    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 10%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-")),
]

groups = [Group(f"{i+1}", label="") for i in range(5)]

for i in groups:
    keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    ),
                ]
            )

layouts = [layout.Columns(
    border_focus='#89b4fa', 
    border_width=2,
    border_on_single=True,
    fair = True,
    margin=[10, 0, 0, 10],
    ),
]

widget_defaults = dict(
    font="FiraCode",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper='~/Pictures/Wallpaper/11.jpg',
        wallpaper_mode='stretch',
        right = bar.Gap(10),
        bottom = bar.Gap(10),
        # left = bar.Gap(10),
        top =bar.Bar(
            [
                widget.Spacer(
                    length=10,
                ),
                widget.GroupBox(
                    borderwidth=0,
                    padding=7,
                    disable_drag=True,
                    active="#cba6f7",
                    inactive="#585b70",
                    block_highlight_text_color="#89b4fa",
                ),
                widget.Spacer(),
                widget.Clock(
                    format="<b>%A, %d %B    %I:%M %p</b>",
                    update_interval = 60.0,
                ),
                widget.Spacer(),
                # widget.Systray(),
                widget.Wlan(
                    ethernet_interface="enp7s0",
                    ethernet_message="",
                    interface="wlp0s20f3",
                    format='{essid} {percent:2.0%}'
                ),
                widget.PulseVolume(),
                widget.DoNotDisturb(),
                widget.Backlight(
                    backlight_name='intel_backlight',
                ),
                widget.Volume(
                ),
                widget.Battery(
                    format='{percent:2.0%}',
                ),
                widget.TextBox(
                    '⏻',
                    mouse_callbacks={
                        'Button1': lazy.spawn('alacritty'),
                    },
                ),
                widget.Spacer(
                    length=17,
                ),
            ],
            30,
            background="#1e1e2e",
        ),
        
        # x11_drag_polling_rate = 60,           You can uncomment this variable if you see that on X11 floating resize/moving is laggy
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    # Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus="#89b4fa",
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
