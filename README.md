# DoEr

---

## Models

#### User
- username
- first_name
- last_name
- email
- joined
- edited

#### Profile
- dp : ImageField
- phone : CharField
- about : TextField
- gender : ChoiceField
- bday : DateField
- user : OnetoOne

#### Group
- title : CharField
- user : ForeignKey
- created_on : DeateField
- done : BoolField
- public : BoolField

#### Entry
- image : ImageField
- heading : Charfield
- content : TextField
- group : ForeignKey
- done : BoolField
- edited  : Datefield
- created : Datefiled
- public : BoolField

---

## Urls
- stats (just inside the public profile)
- profile
- signup
- login
- logout

- dash
- group/[group name]
- group/[group name]/[entry name]

#### Extras
- search page for entries
- search page for users
- search in followers and following
- email verification