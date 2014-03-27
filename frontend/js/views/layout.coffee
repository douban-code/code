define([
  'jquery',
  'backbone',
  'handlebars',
  'views/partials/status'],
  ($, Backbone, Handlebars, StatusView) ->
    Backbone.View.extend({
      initialize: () ->
      statusContainer: () -> $("#statusBar")
      render: () ->
        window.view = new StatusView(el: @statusContainer())
    })
)
