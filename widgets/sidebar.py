def on_team_click(self, team):
    app = self.get_root_window().children[0].children[0]
    team_screen = app.manager.get_screen('team')
    team_screen.current_team = team['name']  # Takım adını sakla
    app.manager.current = 'team' 