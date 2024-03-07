# Lights Maintenance Dashboard

<section>

## Video Demo:

https://youtu.be/Kaedpqxy0jU

</section>
<br><br>

## Description:

#### Summary:

> This lights maintenance dashboard was requested by a client and allows the user to see the status of all lights in a building at a glance, with a table of repair statuses linked to a blueprint diagram

<br>

#### Disclaimers:

> **[Overall]**
>
> 1. This project was created purely using Excel including VBA
> 2. The blueprint in the file is a fictitious one meant for illustration purposes only, the real blueprint used for daily operations is kept confidential

> **[Date picker]**
> The date picker was created by folks at https://sites.google.com/site/e90e50/calendar-control-class and adapted for use in this project.

<br>

#### Main Features:

> 1. **[Initial Data Entry]**
>    Clicking on the light nodes (little circles) in the map prompts a popup. At the top of the pop-up, the serial number of the light is updated, as well as the description of the location of the light. Service staff can input the 1) Status of the light _(Dropdown)_, 2) Report date _(Date picker)_, and 3) Sign off with their name _(Dropdown)_. These details then get transfered into the main database when users hit the save button.

> 2. **[Subsequent Data Entry]**
>    In the event the light is unserviceable, the service staff can go and service it on a separate day, hence when the light node is clicked a second time, the details on the form will be documented in the columns to the right of the table

> 3. **[Table-Diagram Connection Feature 1]**
>    When the light is selected in the table in Column B, that particular light node changes to red while the other light nodes remain yellow to highlight where the light selected is located.

> 4. **[Table-Diagram Connection Feature 2]**
>    When the Serviceability status is updated in a data entry, the text within that light node in the diagram changes to S for servicable and U for unserviceable respectively.

> 5. **[Amending the number of light nodes]**
>    To make this Dashboard more dynamic where users can change the blueprint and create and delete light nodes where necessary, there are buttons to create and delete light nodes above the table

> 6. **[Amending the service staff names]**
>    Users can amend the service staff names by going to the Dropdown tab and changing the names in Column B accordingly.

> 7. **[Changing blueprints]**
>    When changing the blueprint, one just needs to copy the blueprint as a picture into the excel file and send it to the back. Also, it would be best to set the property of the image to "Don't move or size with cells"

<br><br>

## References

1. Grey Background: https://professionals.tarkett.com.au/en_AU/collection-C000187-protectwall-1-5mm/tisse-light-grey
2. Excel VBA Datepicker: https://sites.google.com/site/e90e50/calendar-control-class
3. Example Blueprint: <a href = "https://www.vecteezy.com/free-vector/building-blueprint">Building Blueprint Vectors by Vecteezy</a>
