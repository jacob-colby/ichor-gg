---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.36
  aspect_win_rate: 0.42
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.26
    win_rate: 0.32
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.09
      win_rate: 0.7
    - name: Jotunn's Revenge
      pick_rate: 0.06
      win_rate: 0.67
  - name: Prophetic Cloak
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.41
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.86
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.29
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.33
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.0
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.22
    - name: Soul Reaver
      pick_rate: 0.05
      win_rate: 0.2
  - name: Heartseeker
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.2
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.4
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.2
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.0
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.33
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.36
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.32
    win_rate: 0.38
  - name: Bumba's Golden Dagger
    pick_rate: 0.09
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-08-22'
  god_win_rate: 0.4056603773584906
  god_matches_won: 43
  god_matches_played: 106
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-22'
  god_matches_analyzed: 14126
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Prophetic Cloak
  - Daybreak Gavel
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Daybreak Gavel, Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Breastplate of Valor, Gluttonous Grimoire, Shield Splitter, Spear of
    Desolation, Runeforged Hammer, Spear of the Magus, Helm of Radiance, Soul Gem,
    Berserker''s Shield, Obsidian Shard, Eye of the Storm, Erosion, Eye of Providence,
    Hydra''s Lament, Draconic Scale, Shield of the Phoenix, Stone of Binding, Rod
    of Asclepius, Magi''s Cloak, Avenging Blade, Jade Scepter, Doom Orb, Screeching
    Gargoyle, Wish-Granting Pearl, Mantle Of Discord, Helm of Darkness, Midgardian
    Mail, Titan''s Bane, Death Metal, Chronos'' Pendant, The Crusher, The World Stone,
    Hide of the Nemean Lion, Freya''s Tears.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.06
      fit: 0.4
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.56
      win: 0.33
      pick: 0.0
      fit: 0.55
    Prophetic Cloak:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.11
      fit: 0.4
    Daybreak Gavel:
      total: 0.55
      efficiency: 0.59
      win: 0.7
      pick: 0.09
      fit: 0.13
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.52
    Amanita Charm:
      total: 0.44
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.45
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Prophetic Cloak
  - Daybreak Gavel
  - Heartseeker
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Prophetic Cloak
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Daybreak Gavel, Rod of Tahuti, Amanita Charm, Breastplate of Valor, Gluttonous
    Grimoire, Kinetic Cuirass, Spear of Desolation, Shield Splitter, Spear of the
    Magus, Hydra''s Lament, Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian
    Shard, Berserker''s Shield, Eye of the Storm, Rod of Asclepius, Wish-Granting
    Pearl, Doom Orb, Ancient Signet, The World Stone, Shield of the Phoenix, Erosion,
    Death Metal, Chronos'' Pendant, Jade Scepter, Stone of Binding, Eye of Providence,
    Avenging Blade, Draconic Scale, Screeching Gargoyle, Magi''s Cloak, Titan''s Bane,
    Helm of Darkness, Triton''s Conch, The Crusher, Oni Hunter''s Garb, Freya''s Tears.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.06
      fit: 0.45
    Prophetic Cloak:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.11
      fit: 0.35
    Daybreak Gavel:
      total: 0.54
      efficiency: 0.59
      win: 0.7
      pick: 0.09
      fit: 0.1
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.56
    Rod of Tahuti:
      total: 0.5
      efficiency: 0.86
      win: 0.33
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Prophetic Cloak
  - Transcendence
  - Daybreak Gavel
  - Heartseeker
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Daybreak Gavel, Rod of Tahuti, Amanita Charm, Breastplate
    of Valor, Gluttonous Grimoire, Spear of Desolation, Kinetic Cuirass, Soul Gem,
    Spear of the Magus, Obsidian Shard, Shield Splitter, Runeforged Hammer, Helm of
    Radiance, Berserker''s Shield, Hydra''s Lament, Shield of the Phoenix, Eye of
    the Storm, Erosion, Doom Orb, Rod of Asclepius, Eye of Providence, Screeching
    Gargoyle, Stone of Binding, Chronos'' Pendant, Draconic Scale, The World Stone,
    Titan''s Bane, The Crusher, Dreamer''s Idol, Magi''s Cloak, Jade Scepter, The
    Reaper, Wish-Granting Pearl, Avenging Blade, Mantle Of Discord, Midgardian Mail,
    Ancient Signet, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.35
      efficiency: 0.51
      win: 0.33
      pick: 0.0
      fit: 0.14
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.67
      pick: 0.06
      fit: 0.48
    Prophetic Cloak:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.11
      fit: 0.41
    Transcendence:
      total: 0.35
      efficiency: 0.53
      win: 0.33
      pick: 0.0
      fit: 0.14
    Daybreak Gavel:
      total: 0.54
      efficiency: 0.59
      win: 0.7
      pick: 0.09
      fit: 0.11
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Daybreak Gavel
  - Heartseeker
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Amanita Charm
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Daybreak Gavel, Rod of Tahuti, Amanita Charm, Soul
    Gem, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire, Kinetic Cuirass,
    Ethereal Staff, Breastplate of Valor, The Reaper, Runeforged Hammer, Spear of
    Desolation, Spear of the Magus, Shield Splitter, Berserker''s Shield, Lifebinder,
    Obsidian Shard, Helm of Radiance, Eye of the Storm, Yogi''s Necklace, Sphere of
    Negation, Hydra''s Lament, Erosion, Phoenix Feather, Eye of Providence, Chandra''s
    Grace, Draconic Scale, Avenging Blade, Blood-Bound Book, Jade Scepter, Wish-Granting
    Pearl, Stone of Binding, Doom Orb, Glorious Pridwen, Midgardian Mail, Titan''s
    Bane, Freya''s Tears.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.06
      fit: 0.42
    Daybreak Gavel:
      total: 0.55
      efficiency: 0.59
      win: 0.7
      pick: 0.09
      fit: 0.16
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.53
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.86
      win: 0.33
      pick: 0.0
      fit: 0.31
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.45
      efficiency: 0.52
      win: 0.33
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Prophetic Cloak
  - Daybreak Gavel
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Daybreak Gavel, Rod of Tahuti, Amanita Charm,
    Gluttonous Grimoire, Stone of Binding, Spear of Desolation, Spear of the Magus,
    Avenging Blade, Kinetic Cuirass, Screeching Gargoyle, Soul Gem, Breastplate of
    Valor, Obsidian Shard, Void Shield, Void Stone, Shield Splitter, Runeforged Hammer,
    Helm of Radiance, Berserker''s Shield, Doom Orb, Titan''s Bane, The Crusher, The
    World Stone, Eye of the Storm, Hydra''s Lament, Dreamer''s Idol, Erosion, The
    Reaper, Eye of Providence, Rod of Asclepius, Shield of the Phoenix, Draconic Scale,
    Magi''s Cloak, Jade Scepter, Wish-Granting Pearl, Mantle Of Discord, Midgardian
    Mail, Freya''s Tears.'
  slot_scores:
    Stone of Binding:
      total: 0.43
      efficiency: 0.51
      win: 0.33
      pick: 0.0
      fit: 0.67
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.67
      pick: 0.06
      fit: 0.49
    Prophetic Cloak:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.11
      fit: 0.34
    Daybreak Gavel:
      total: 0.54
      efficiency: 0.59
      win: 0.7
      pick: 0.09
      fit: 0.11
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.62
    Amanita Charm:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Daybreak Gavel
  - Nimble Ring
  - Heartseeker
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Daybreak Gavel, Rod of Tahuti, Berserker''s Shield,
    Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul Gem, Breastplate of Valor,
    Kinetic Cuirass, Golden Blade, Riptalon, Spear of the Magus, Spear of Desolation,
    Silverbranch Bow, Helm of Radiance, Runeforged Hammer, Tyrfing, Shield Splitter,
    Obsidian Shard, Lernaean Bow, Pharaoh''s Curse, Toxic Blade, Shogun''s Ofuda,
    The Reaper, Rod of Asclepius, Hydra''s Lament, Stone of Binding, Erosion, Tekko-Kagi,
    Bragi''s Harp, Shield of the Phoenix, Eye of Providence, Eye of the Storm, Bracer
    of The Abyss, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.4
      efficiency: 0.52
      win: 0.33
      pick: 0.0
      fit: 0.45
    Berserker's Shield:
      total: 0.44
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.67
      pick: 0.06
      fit: 0.25
    Daybreak Gavel:
      total: 0.54
      efficiency: 0.59
      win: 0.7
      pick: 0.09
      fit: 0.09
    Nimble Ring:
      total: 0.42
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.33
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Prophetic Cloak
  - Daybreak Gavel
  - Heartseeker
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Daybreak Gavel,
    Rod of Tahuti, Prophetic Cloak, Breastplate of Valor, Amanita Charm, Spear of
    Desolation, Kinetic Cuirass, Soul Gem, Shield of the Phoenix, Hydra''s Lament,
    Screeching Gargoyle, Gluttonous Grimoire, Berserker''s Shield, Chronos'' Pendant,
    Shield Splitter, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Erosion,
    Obsidian Shard, Eye of Providence, Stone of Binding, Draconic Scale, Gladiator''s
    Shield, Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius,
    Eye of Erebus, Mantle Of Discord, Midgardian Mail, Pendulum Blade, Hide of the
    Nemean Lion, Glorious Pridwen, Jade Scepter, Chandra''s Grace, Freya''s Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.44
      efficiency: 0.66
      win: 0.29
      pick: 0.26
      fit: 0.43
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.65
      win: 0.33
      pick: 0.14
      fit: 0.43
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.67
      pick: 0.06
      fit: 0.51
    Prophetic Cloak:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.11
      fit: 0.58
    Daybreak Gavel:
      total: 0.54
      efficiency: 0.59
      win: 0.7
      pick: 0.09
      fit: 0.12
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.42
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
    of Providence, Hydra''s Lament, Draconic Scale, Shield of the Phoenix, Stone of
    Binding, Rod of Asclepius, Magi''s Cloak, Avenging Blade, Jade Scepter, Doom Orb,
    Screeching Gargoyle, Wish-Granting Pearl, Mantle Of Discord, Helm of Darkness,
    Midgardian Mail, Titan''s Bane, Death Metal, Chronos'' Pendant, The Crusher, Daybreak
    Gavel, The World Stone, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.41
      efficiency: 0.66
      win: 0.29
      pick: 0.26
      fit: 0.24
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.06
      fit: 0.4
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.56
      win: 0.33
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.28
      efficiency: 0.61
      win: 0.0
      pick: 0.12
      fit: 0.4
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.86
      win: 0.33
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.44
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.45
  starter: *id001
---
