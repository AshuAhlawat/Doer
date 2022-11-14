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
- email verification

- different delete options on the groupings delete page
- add different error page that redirects back in some time and displays error

- implement sort as model
- can edit their default sort in profile page
- implement search/filter/sort on all entries/groupings
- trash feature

- make default profile public, and then an edit button that only shows up for your page
- make about 10 people show up on follower page, and then a view all link that shows all people
- view all details of entries button on progile page