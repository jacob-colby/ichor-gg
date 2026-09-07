---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.23
  aspect_win_rate: 0.48
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.21
    win_rate: 0.33
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.14
      win_rate: 0.52
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.42
  - name: Breastplate of Valor
    pick_rate: 0.1
    win_rate: 0.42
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.5
    - name: Chronos' Pendant
      pick_rate: 0.08
      win_rate: 0.13
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.44
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.29
  - name: Rod of Tahuti
    pick_rate: 0.07
    win_rate: 0.23
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.38
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.5
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.38
    - name: Brawler’s Beat Stick
      pick_rate: 0.04
      win_rate: 0.43
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.56
    alternates:
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.4
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.6
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.56
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.44
  - name: Pendulum of the Ages
    pick_rate: 0.15
    win_rate: 0.32
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-09-07'
  god_win_rate: 0.43157894736842106
  god_matches_won: 82
  god_matches_played: 190
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-07'
  god_matches_analyzed: 16223
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Draconic Scale, Kinetic Cuirass, Daybreak
    Gavel, Breastplate of Valor, Gluttonous Grimoire, Shield Splitter, Rod of Tahuti,
    Spear of Desolation, Runeforged Hammer, Spear of the Magus, Helm of Radiance,
    Soul Gem, Berserker''s Shield, Obsidian Shard, Eye of the Storm, Erosion, Eye
    of Providence, Hydra''s Lament, Heartseeker, Shield of the Phoenix, Stone of Binding,
    Rod of Asclepius, Magi''s Cloak, Avenging Blade, Jade Scepter, Doom Orb, Screeching
    Gargoyle, Wish-Granting Pearl, Mantle Of Discord, Helm of Darkness, Midgardian
    Mail, Titan''s Bane, Death Metal, The Crusher, The World Stone, Freya''s Tears,
    Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.24
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.42
      pick: 0.0
      fit: 0.55
    Hide of the Nemean Lion:
      total: 0.49
      efficiency: 0.52
      win: 0.56
      pick: 0.28
      fit: 0.29
    Draconic Scale:
      total: 0.47
      efficiency: 0.5
      win: 0.5
      pick: 0.11
      fit: 0.45
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Daybreak Gavel
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Daybreak Gavel
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Amanita Charm, Breastplate of Valor, Daybreak Gavel, Rod of Tahuti, Draconic
    Scale, Gluttonous Grimoire, Kinetic Cuirass, Spear of Desolation, Shield Splitter,
    Spear of the Magus, Hydra''s Lament, Runeforged Hammer, Helm of Radiance, Soul
    Gem, Obsidian Shard, Heartseeker, Berserker''s Shield, Eye of the Storm, Rod of
    Asclepius, Wish-Granting Pearl, Doom Orb, Ancient Signet, The World Stone, Shield
    of the Phoenix, Erosion, Death Metal, Jade Scepter, Stone of Binding, Eye of Providence,
    Avenging Blade, Screeching Gargoyle, Magi''s Cloak, Titan''s Bane, Helm of Darkness,
    Triton''s Conch, The Crusher, Oni Hunter''s Garb, Freya''s Tears, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.29
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.65
      win: 0.42
      pick: 0.14
      fit: 0.29
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.45
    Daybreak Gavel:
      total: 0.46
      efficiency: 0.59
      win: 0.52
      pick: 0.14
      fit: 0.1
    Hide of the Nemean Lion:
      total: 0.48
      efficiency: 0.52
      win: 0.56
      pick: 0.28
      fit: 0.23
    Amanita Charm:
      total: 0.47
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Daybreak Gavel
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Amanita Charm, Breastplate of Valor, Daybreak Gavel, Gluttonous
    Grimoire, Draconic Scale, Spear of Desolation, Rod of Tahuti, Kinetic Cuirass,
    Soul Gem, Spear of the Magus, Obsidian Shard, Shield Splitter, Runeforged Hammer,
    Helm of Radiance, Berserker''s Shield, Hydra''s Lament, Heartseeker, Shield of
    the Phoenix, Eye of the Storm, Erosion, Doom Orb, Rod of Asclepius, Eye of Providence,
    Screeching Gargoyle, Stone of Binding, The World Stone, Titan''s Bane, The Crusher,
    Dreamer''s Idol, Magi''s Cloak, Jade Scepter, The Reaper, Wish-Granting Pearl,
    Avenging Blade, Freya''s Tears, Mantle Of Discord, Midgardian Mail, Ancient Signet,
    Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.39
      efficiency: 0.51
      win: 0.42
      pick: 0.1
      fit: 0.14
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.27
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.48
    Transcendence:
      total: 0.39
      efficiency: 0.53
      win: 0.42
      pick: 0.0
      fit: 0.14
    Hide of the Nemean Lion:
      total: 0.48
      efficiency: 0.52
      win: 0.56
      pick: 0.28
      fit: 0.25
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Book of Thoth
  - Genji's Guard
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Daybreak Gavel
  - Hide of the Nemean Lion
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Daybreak Gavel
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Soul Gem, Rod of Asclepius, Shield
    of the Phoenix, Daybreak Gavel, Draconic Scale, Gluttonous Grimoire, Kinetic Cuirass,
    Ethereal Staff, Breastplate of Valor, The Reaper, Rod of Tahuti, Runeforged Hammer,
    Spear of Desolation, Spear of the Magus, Shield Splitter, Berserker''s Shield,
    Lifebinder, Obsidian Shard, Helm of Radiance, Eye of the Storm, Yogi''s Necklace,
    Sphere of Negation, Hydra''s Lament, Erosion, Heartseeker, Phoenix Feather, Eye
    of Providence, Chandra''s Grace, Avenging Blade, Blood-Bound Book, Jade Scepter,
    Wish-Granting Pearl, Stone of Binding, Doom Orb, Glorious Pridwen, Midgardian
    Mail, Titan''s Bane, Freya''s Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.22
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.42
    Daybreak Gavel:
      total: 0.47
      efficiency: 0.59
      win: 0.52
      pick: 0.14
      fit: 0.16
    Hide of the Nemean Lion:
      total: 0.49
      efficiency: 0.52
      win: 0.56
      pick: 0.28
      fit: 0.3
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.49
      efficiency: 0.52
      win: 0.42
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Genji's Guard
  - Daybreak Gavel
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Daybreak Gavel
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Daybreak Gavel
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Rod of Tahuti,
    Stone of Binding, Daybreak Gavel, Draconic Scale, Spear of Desolation, Spear of
    the Magus, Avenging Blade, Kinetic Cuirass, Screeching Gargoyle, Soul Gem, Breastplate
    of Valor, Obsidian Shard, Void Shield, Heartseeker, Void Stone, Shield Splitter,
    Runeforged Hammer, Helm of Radiance, Berserker''s Shield, Doom Orb, Titan''s Bane,
    The Crusher, The World Stone, Eye of the Storm, Hydra''s Lament, Dreamer''s Idol,
    Erosion, The Reaper, Eye of Providence, Rod of Asclepius, Shield of the Phoenix,
    Magi''s Cloak, Jade Scepter, Wish-Granting Pearl, Mantle Of Discord, Midgardian
    Mail, Freya''s Tears.'
  slot_scores:
    Stone of Binding:
      total: 0.47
      efficiency: 0.51
      win: 0.42
      pick: 0.0
      fit: 0.67
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.21
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.49
    Daybreak Gavel:
      total: 0.46
      efficiency: 0.59
      win: 0.52
      pick: 0.14
      fit: 0.11
    Hide of the Nemean Lion:
      total: 0.48
      efficiency: 0.52
      win: 0.56
      pick: 0.28
      fit: 0.25
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Daybreak Gavel
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Hide of the Nemean Lion
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Gluttonous Grimoire, Nimble
    Ring, Amanita Charm, Daybreak Gavel, Draconic Scale, Soul Gem, Breastplate of
    Valor, Kinetic Cuirass, Rod of Tahuti, Golden Blade, Riptalon, Spear of the Magus,
    Spear of Desolation, Silverbranch Bow, Helm of Radiance, Runeforged Hammer, Tyrfing,
    Shield Splitter, Obsidian Shard, Lernaean Bow, Pharaoh''s Curse, Toxic Blade,
    Shogun''s Ofuda, The Reaper, Rod of Asclepius, Hydra''s Lament, Stone of Binding,
    Erosion, Tekko-Kagi, Bragi''s Harp, Shield of the Phoenix, Eye of Providence,
    Eye of the Storm, Bracer of The Abyss, Heartseeker, Magi''s Cloak, Screeching
    Gargoyle, Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.52
      win: 0.42
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.17
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.42
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.47
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.33
    Hide of the Nemean Lion:
      total: 0.48
      efficiency: 0.52
      win: 0.56
      pick: 0.28
      fit: 0.2
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Breastplate of
    Valor, Amanita Charm, Spear of Desolation, Draconic Scale, Daybreak Gavel, Kinetic
    Cuirass, Soul Gem, Shield of the Phoenix, Hydra''s Lament, Screeching Gargoyle,
    Gluttonous Grimoire, Rod of Tahuti, Berserker''s Shield, Shield Splitter, Freya''s
    Tears, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Prophetic Cloak,
    Erosion, Obsidian Shard, Eye of Providence, Stone of Binding, Gladiator''s Shield,
    Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Heartseeker,
    Eye of Erebus, Mantle Of Discord, Midgardian Mail, Pendulum Blade, Glorious Pridwen,
    Jade Scepter, Chandra''s Grace, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.43
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.42
      pick: 0.14
      fit: 0.43
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.51
    Hide of the Nemean Lion:
      total: 0.49
      efficiency: 0.52
      win: 0.56
      pick: 0.28
      fit: 0.26
    Spear of Desolation:
      total: 0.47
      efficiency: 0.57
      win: 0.42
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Kinetic
    Cuirass, Freya''s Tears, Gluttonous Grimoire, Shield Splitter, Breastplate of
    Valor, Spear of Desolation, Runeforged Hammer, Spear of the Magus, Helm of Radiance,
    Soul Gem, Berserker''s Shield, Obsidian Shard, Eye of the Storm, Erosion, Eye
    of Providence, Hydra''s Lament, Draconic Scale, Heartseeker, Shield of the Phoenix,
    Stone of Binding, Rod of Asclepius, Magi''s Cloak, Avenging Blade, Jade Scepter,
    Doom Orb, Screeching Gargoyle, Wish-Granting Pearl, Mantle Of Discord, Helm of
    Darkness, Midgardian Mail, Titan''s Bane, Death Metal, Chronos'' Pendant, The
    Crusher, Daybreak Gavel, The World Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.25
      fit: 0.24
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.42
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.41
      efficiency: 0.61
      win: 0.29
      pick: 0.11
      fit: 0.4
    Rod of Tahuti:
      total: 0.45
      efficiency: 0.86
      win: 0.23
      pick: 0.12
      fit: 0.3
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
---
