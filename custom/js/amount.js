/**
 * Created by swannsg on 2015/04/23.
 */
// usage in html
//<div class="form-group">
//<label for="amount" class="col-sm-2 control-label">Amount</label>
//<div class="col-sm-10">
//<input type="text" class="form-control" id="amount" title="Amount including VAT" required pattern="\d+(.\d{0,2})?">
//</div>
//</div>
jQuery(function($) {
    $('#amount').autoNumeric('init');
});