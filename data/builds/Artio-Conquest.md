---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.5
  aspect_win_rate: 0.59
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.18
    win_rate: 0.51
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.15
      win_rate: 0.57
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 0.47
  - name: Breastplate of Valor
    pick_rate: 0.09
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.5
    - name: Prophetic Cloak
      pick_rate: 0.08
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.53
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.4
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.52
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.46
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.35
  - name: Hide of the Nemean Lion
    pick_rate: 0.04
    win_rate: 0.39
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.68
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.57
  - name: Olmec Blue
    pick_rate: 0.06
    win_rate: 0.6
    alternates:
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.71
    - name: Mote of Chaos
      pick_rate: 0.04
      win_rate: 0.58
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.22
    win_rate: 0.54
  - name: Bumba's Cudgel
    pick_rate: 0.14
    win_rate: 0.36
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-11-03'
  god_win_rate: 0.5303326810176126
  god_matches_won: 271
  god_matches_played: 511
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Shield Splitter, Jotunn''s Revenge, Kinetic
    Cuirass, Berserker''s Shield, Gluttonous Grimoire, Runeforged Hammer, Soul Gem,
    Hydra''s Lament, Erosion, Eye of Providence, Oni Hunter''s Garb, Draconic Scale,
    The Reaper, Shield of the Phoenix, Stone of Binding, Helm of Radiance, Midgardian
    Mail, Helm of Darkness, Avenging Blade, Titan''s Bane, Magi''s Cloak, Spear of
    Desolation, Leviathan''s Hide, Screeching Gargoyle, Breastplate of Valor, Mantle
    Of Discord, Wyrmskin Hide, Arondight, Obsidian Shard, Blood-Bound Book, Ancile,
    Death Metal, Sanguine Lash, Stampede, Void Stone, Void Shield, Hide of the Nemean
    Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.6
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.23
      fit: 0.45
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Soul Gem, Shield of the Phoenix, The Reaper,
    Jotunn''s Revenge, Kinetic Cuirass, Berserker''s Shield, Shield Splitter, Gluttonous
    Grimoire, Blood-Bound Book, Runeforged Hammer, Phoenix Feather, Yogi''s Necklace,
    Bloodforge, Ethereal Staff, Hydra''s Lament, Oni Hunter''s Garb, Erosion, Chandra''s
    Grace, Eye of Providence, Draconic Scale, Avenging Blade, Bancroft''s Talon, Midgardian
    Mail, Regrowth Striders, Rod of Asclepius, Titan''s Bane, Leviathan''s Hide, Helm
    of Radiance, Glorious Pridwen, Sphere of Negation, Wyrmskin Hide, Spear of Desolation,
    Stone of Binding, Helm of Darkness, Soul Locket, Screeching Gargoyle, Breastplate
    of Valor.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.23
      fit: 0.41
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Stone of Binding
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Gluttonous Grimoire, Soul Gem,
    Amanita Charm, Stone of Binding, The Reaper, Avenging Blade, Screeching Gargoyle,
    Berserker''s Shield, Titan''s Bane, Shield Splitter, Spear of Desolation, Obsidian
    Shard, Kinetic Cuirass, Void Stone, Void Shield, The Crusher, Runeforged Hammer,
    Spear of the Magus, Heartseeker, Hydra''s Lament, Oni Hunter''s Garb, Doom Orb,
    Erosion, Helm of Radiance, Eye of Providence, Tekko-Kagi, The World Stone, Shield
    of the Phoenix, Midgardian Mail, Draconic Scale, Helm of Darkness, Magi''s Cloak,
    Breastplate of Valor, Dreamer''s Idol, Leviathan''s Hide, Blood-Bound Book, Mantle
    Of Discord, Arondight.'
  slot_scores:
    Stone of Binding:
      total: 0.52
      efficiency: 0.5
      win: 0.55
      pick: 0.0
      fit: 0.66
    Avenging Blade:
      total: 0.52
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.67
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.6
      pick: 0.23
      fit: 0.33
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.55
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Nimble Ring, Jotunn''s
    Revenge, Golden Blade, Kinetic Cuirass, Shield Splitter, Gluttonous Grimoire,
    Tyrfing, Soul Gem, Tekko-Kagi, Runeforged Hammer, Pharaoh''s Curse, Lernaean Bow,
    Toxic Blade, Silverbranch Bow, Eros'' Bow, Hydra''s Lament, Oni Hunter''s Garb,
    Shogun''s Ofuda, Helm of Radiance, Erosion, Eye of Providence, Obsidian Shard,
    Spear of Desolation, The Reaper, Midgardian Mail, Shield of the Phoenix, Stone
    of Binding, Draconic Scale, Riptalon, Titan''s Bane, Dominance, Screeching Gargoyle,
    Helm of Darkness, Breastplate of Valor, Magi''s Cloak, Bragi''s Harp, Blood-Bound
    Book.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.55
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.53
      pick: 0.17
      fit: 0.19
    Berserker's Shield:
      total: 0.57
      efficiency: 0.74
      win: 0.55
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.51
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.6
      pick: 0.23
      fit: 0.31
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Soul Gem, Amanita Charm, Spear of Desolation, Berserker''s Shield, Kinetic Cuirass,
    Gluttonous Grimoire, Prophetic Cloak, Hydra''s Lament, Shield of the Phoenix,
    Screeching Gargoyle, Shield Splitter, Breastplate of Valor, Lotus Sickle, Chronos''
    Pendant, Arondight, Runeforged Hammer, Helm of Radiance, Oni Hunter''s Garb, Obsidian
    Shard, Erosion, Helm of Darkness, Eye of Providence, Gem of Focus, Gladiator''s
    Shield, Heartwood Charm, Draconic Scale, Blood-Bound Book, Midgardian Mail, Stone
    of Binding, Magi''s Cloak, The Reaper, Leviathan''s Hide, Chandra''s Grace, Eye
    of Erebus, Ancient Signet, Regrowth Striders, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.53
      pick: 0.17
      fit: 0.44
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.6
      pick: 0.23
      fit: 0.58
    Spear of Desolation:
      total: 0.52
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.55
      pick: 0.0
      fit: 0.13
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Gluttonous Grimoire, Kinetic Cuirass,
    Soul Gem, Runeforged Hammer, The Reaper, Tekko-Kagi, Titan''s Bane, Hydra''s Lament,
    Golden Blade, Nimble Ring, Spear of Desolation, Obsidian Shard, The Crusher, Tyrfing,
    Lernaean Bow, Oni Hunter''s Garb, Avenging Blade, Heartseeker, Helm of Radiance,
    Erosion, Eye of Providence, Arondight, Shield of the Phoenix, Midgardian Mail,
    Draconic Scale, Stone of Binding, Spear of the Magus, Death Metal, Toxic Blade,
    Helm of Darkness, Pharaoh''s Curse, Screeching Gargoyle, Magi''s Cloak, Breastplate
    of Valor, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.53
      pick: 0.17
      fit: 0.2
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.55
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.43
    Shield Splitter:
      total: 0.52
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.6
      pick: 0.23
      fit: 0.33
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    Jotunn''s Revenge, Soul Gem, Amanita Charm, Shield Splitter, Berserker''s Shield,
    Kinetic Cuirass, Obsidian Shard, Spear of Desolation, Runeforged Hammer, The Reaper,
    Helm of Radiance, Titan''s Bane, Spear of the Magus, Hydra''s Lament, Helm of
    Darkness, Blood-Bound Book, Death Metal, Ancient Signet, Oni Hunter''s Garb, Lotus
    Sickle, The Crusher, Erosion, Doom Orb, Jade Scepter, Eye of Providence, The World
    Stone, Avenging Blade, Shield of the Phoenix, Midgardian Mail, Chronos'' Pendant,
    Stone of Binding, Draconic Scale, Heartseeker, Screeching Gargoyle, Magi''s Cloak,
    Breastplate of Valor, Arondight, Leviathan''s Hide.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.17
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.39
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.17
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.6
      pick: 0.23
      fit: 0.33
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.55
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Shield Splitter, Jotunn''s
    Revenge, Kinetic Cuirass, Berserker''s Shield, Gluttonous Grimoire, Runeforged
    Hammer, Breastplate of Valor, Soul Gem, Hydra''s Lament, Erosion, Eye of Providence,
    Oni Hunter''s Garb, Draconic Scale, The Reaper, Shield of the Phoenix, Stone of
    Binding, Helm of Radiance, Midgardian Mail, Helm of Darkness, Avenging Blade,
    Titan''s Bane, Magi''s Cloak, Spear of Desolation, Leviathan''s Hide, Screeching
    Gargoyle, Mantle Of Discord, Wyrmskin Hide, Arondight, Obsidian Shard, Blood-Bound
    Book, Ancile, Death Metal, Hide of the Nemean Lion, Sanguine Lash, Stampede, Void
    Stone, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.53
      pick: 0.17
      fit: 0.27
    Berserker's Shield:
      total: 0.53
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.67
      win: 0.55
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.6
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  starter: *id001
---
