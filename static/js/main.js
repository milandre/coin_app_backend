/* Service functions */

function getClientAccounts(url){

	$.ajax({
        url: url,
        method: 'GET'
    }).done(function(data){

    	accounts_html = '';

    	data.forEach(function(account) {
            accounts_html += '<div class="panel panel-default">'
	        accounts_html += '<div class="panel-body">'
	        accounts_html += '<div class="col-6"><span>Currency: '+ account['currency']['currency_id'] +'</span></div>'
	        accounts_html += '<div class="col-6"><span>Balance: '+ account['balance'] +'</span></div>'
	        accounts_html += '</div></div><hr>'
        });    	

    	$('#account-list').empty();
        $('#account-list').prepend(accounts_html);

    }).fail( function(jqXHR, textStatus, errorThrown ) {

        alert(textStatus);
    });


}


function getClientTransactions(url){

	$.ajax({
        url: url,
        method: 'GET'
    }).done(function(data){

    	transaction_html = '';

    	data.forEach(function(transaction) {
            transaction_html += '<div class="panel panel-default"><div class="panel-body" style="display: inline-flex;"><div class="col-sm-4 text-center">';
	        transaction_html += '<h3>From </h3><span>'+ transaction['account_from']['client']['first_name'] + '</span></div>';
	        transaction_html += '<div class="col-sm-4 text-center"><h3> To </h3><span>'+ transaction['account_to']['client']['first_name'] +'</span></div><div class="col-sm-4 text-center">';
	        transaction_html += '<h3> Currency </h3><span>'+ transaction['currency']['currency_id'] +'</span></div><div class="col-sm-4 text-center">';
	        transaction_html += '<h3> Amount </h3><span>'+ transaction['amount'] +'</span></div></div></div><hr>'
        });

        if(!transaction_html){
        	transaction_html = '<div class="margin-bottom">You do not have transactions yet</div>'
        }

    	$('#transaction-list').empty();
        $('#transaction-list').prepend(transaction_html);

    }).fail( function(jqXHR, textStatus, errorThrown ) {

        alert(textStatus);
    });

}


/*function createCurrency(url, form_data){

	$.ajax({
        type: "POST",
        url: url,
        data: form_data,
        error: function () {
           
        },
        success: function (data) {
            
        }
    });
}

function listReceivedTransactions(account){

}

function listSendedTransactions(account){

}

function sendMoney(from, to, money){

}*/
