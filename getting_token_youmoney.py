from yoomoney import Authorize

Authorize(
      client_id="", # - тут вставляем client_id, который вы сохранили ранее
      redirect_uri="", # - тут вставляем ссылку на вашего бота, а точнее ту, которую вы указали, как redirected_url
      scope=["account-info",
             "operation-history",
             "operation-details",
             "incoming-transfers",
             "payment-p2p",
             "payment-shop",
             ]
      )