

class Render(oject)

    def render(self, position, steps_counter, force_render=False):
        if self.should_render(force_render):
            empty, padding_end, padding_start, visible_length, visible_tape_section = self.tape_format_calc(index)
            self.print_system_clear()
            self.print_statistics(index, steps_counter)
            self.print_render_mode_information()
            self.print_tape(empty, padding_end, padding_start, visible_length, visible_tape_section)
            self.print_sign_occurrences()
            if self.activate_interactive:
                input()
            if self.speed:
                time.sleep(self.speed)

    def should_render(self, force_render):
        return self.activate_render or self.activate_interactive or force_render

    def print_system_clear(self):
        os.system('clear')
    

    def tape_format_calc(self, index):
        length = len(self.tape)
        visible_length = Config.visible_tape_length()
        empty = Config.empty_character()
        padding_start = visible_length - index
        padding_end = visible_length - (length - (index + 1))
        dynamic_start = index - visible_length if index >= visible_length else 0
        dynamic_end = length - (length - index - visible_length) if length - index > visible_length else length
        visible_tape_section = list_to_string(self.tape)[dynamic_start:dynamic_end]
        return empty, padding_end, padding_start, visible_length, visible_tape_section


    def print_sign_occurrences(self):
        print('Character Counter')
        for character, occurrence in count_occurrences(self.tape).items():
            print('{}x: {}'.format(occurrence, character))

    def print_tape(self, empty, padding_end, padding_start, visible_length, visible_tape_section):
        padding_icons = visible_length * 2 * '='
        print(padding_icons + '▼' + padding_icons)
        print(pipeify(padding_start * empty + visible_tape_section + padding_end * empty))
        print(padding_icons + '▲' + padding_icons)

    def print_render_mode_information(self):
        print('Render Mode')
        text_for_automatic_mode = 'X' if self.activate_render and not self.activate_interactive else ' '
        show_for_interactive_mode = ('X', '(Press enter to render next step...)')
        text_for_interactive_mode = (show_for_interactive_mode if self.activate_interactive else (' ', ' '))
        none_render_activated = not self.activate_interactive and not self.activate_render
        show_for_none_mode = ('X', '(Please wait for results...)')
        text_for_none_mode = (show_for_none_mode if none_render_activated else (' ', ' '))
        print('[{}] Automatic'.format(text_for_automatic_mode))
        print('[{}] Interactive {}'.format(text_for_interactive_mode[0], text_for_interactive_mode[1]))
        print('[{}] None {}'.format(text_for_none_mode[0], text_for_none_mode[1]))

    def print_statistics(self, index, steps_counter):
        print('Steps Counter {}'.format(str(steps_counter).rjust(7)))
        print('Current State {}'.format(self.state.rjust(7)))
        print('Tape Index {} '.format(str(index).rjust(10)))
