# Future Plans

Some features are not ready yet but on the roadmap for the next version.
[issues](https://github.com/rpchabruno/dundie-rewards/issues)

## Commands

- `load`
- `show`
- `add`
- `transfer`
- `history`

## Password portection

All the commands will require e-mail and password, and then will check on the
`users` table to validate the autentication.

## Role Based Acess Control

Users that has `admin` = `True` on the `users` table will be able to run the
commands: `load`, `add` for the users acess is denied.

The `show` command will allow filtering by `dept` and `email` for admins but
for other users will default to `--email=user_email` so the user can see only
his own report.

The `transfer` command will allow user to send points from his own account
to any other and will be password protected.

The `history` command allow user to see his own movements, admin users can
pass `--email=` and see anyone else movements.
