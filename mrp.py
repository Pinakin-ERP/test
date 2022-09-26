def button_mark_done(self):
        res = super(MrpProduction, self).button_mark_done()
        # for order in self:
        #     order._costs_generate()

        # to_reconcile_account_move_lines = vacuum_svl.account_move_id.line_ids.filtered(lambda l: not l.reconciled and l.account_id == accounts['stock_output'] and l.account_id.reconcile)
        # to_reconcile_account_move_lines += new_account_move.line_ids.filtered(lambda l: not l.reconciled and l.account_id == accounts['stock_output'] and l.account_id.reconcile)
        # return to_reconcile_account_move_lines.reconcile()

        if self._context.get('skip_immediate', False):
            valuation_layer=(self.move_raw_ids + self.move_finished_ids + self.scrap_ids.move_id).stock_valuation_layer_ids
            print ('====>>>',valuation_layer,res,valuation_layer.mapped('account_move_id').line_ids)
            to_reconcile = valuation_layer.mapped('account_move_id').line_ids.filtered(lambda l: not l.reconciled and l.account_id.reconcile and l.account_id.code == '23000')
            print ('to_reconcile===>>',to_reconcile)
            to_reconcile.reconcile()
            #print (x)

        #print (x)
        return res
