document.addEventListener('DOMContentLoaded', function ()
{
    $('DIV#add_item').click(function ()
    {
        $('UL.my_list').append('<li>Item</li>');
    });


    $('DIV#remove_item').click(function ()
    {
        $('UL.my_list LI:last-child').remove();
    });


    $('DIV#clear_list').click(function ()
    {
        $('UL.my_list').html('');
    });
}); 
