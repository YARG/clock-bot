from bot.action.core.action import ActionGroup
from bot.action.core.command import CommandAction
from bot.action.core.filter import MessageAction, TextMessageAction, NoPendingAction, PendingAction
from bot.action.standard.admin import RestartAction, EvalAction, AdminActionWithErrorMessage, AdminAction, HaltAction, \
    GroupAdminAction
from bot.action.standard.answer import AnswerAction
from bot.action.standard.chatsettings.action import ChatSettingsAction
from bot.action.standard.config import ConfigAction
from bot.action.standard.internationalization import InternationalizationAction
from bot.action.standard.perchat import PerChatAction
from bot.action.standard.silence import SilenceAction
from bot.bot import Bot


class BotManager:
    def __init__(self):
        self.bot = Bot()

    def setup_actions(self):
        self.bot.set_action(
            ActionGroup(

                NoPendingAction().then(

                    MessageAction().then(
                        PerChatAction().then(
                            InternationalizationAction().then(
                                TextMessageAction().then(

                                    CommandAction("start").then(
                                        AnswerAction(
                                            "Hello! I am " + self.bot.cache.bot_info.first_name + ". Use me in inline mode to get the current time in any place on the world.")
                                    ),

                                    CommandAction("ping").then(
                                        AnswerAction("Up and running, sir!")
                                    ),

                                    CommandAction("restart").then(
                                        AdminActionWithErrorMessage().then(
                                            RestartAction()
                                        )
                                    ),
                                    CommandAction("halt").then(
                                        AdminActionWithErrorMessage().then(
                                            HaltAction()
                                        )
                                    ),
                                    CommandAction("eval").then(
                                        AdminActionWithErrorMessage().then(
                                            EvalAction()
                                        )
                                    ),
                                    CommandAction("config").then(
                                        AdminActionWithErrorMessage().then(
                                            ConfigAction()
                                        )
                                    ),

                                    CommandAction("settings").then(
                                        GroupAdminAction().then(
                                            ChatSettingsAction()
                                        )
                                    ),

                                    CommandAction("silence").then(
                                        GroupAdminAction().then(
                                            SilenceAction()
                                        )
                                    )

                                )
                            )
                        )
                    )

                ),

                PendingAction().then(
                    MessageAction().then(
                        PerChatAction().then(
                            TextMessageAction().then(

                                CommandAction("ping").then(
                                    AnswerAction("I'm back! Sorry for the delay...")
                                ),

                                AdminAction().then(
                                    CommandAction("restart").then(
                                        RestartAction()
                                    ),
                                    CommandAction("halt").then(
                                        HaltAction()
                                    )
                                )

                            )
                        )
                    )
                )

            )
        )

    def run(self):
        self.bot.run()