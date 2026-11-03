---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.28
  slot_order:
  - name: Runeforged Hammer
    pick_rate: 0.41
    win_rate: 0.61
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.63
  - name: Breastplate of Valor
    pick_rate: 0.15
    win_rate: 0.67
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.74
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.59
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.56
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.65
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.69
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.62
  - name: Kinetic Cuirass
    pick_rate: 0.07
    win_rate: 0.65
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.66
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.55
  - name: Sage's Ring
    pick_rate: 0.09
    win_rate: 0.89
    alternates:
    - name: Veve Charm
      pick_rate: 0.08
      win_rate: 0.61
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.71
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.32
    win_rate: 0.62
  - name: Bumba's Cudgel
    pick_rate: 0.3
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.09
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-11-03'
  god_win_rate: 0.5677749360613811
  god_matches_won: 222
  god_matches_played: 391
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
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Shield Splitter, Jotunn''s Revenge, Berserker''s
    Shield, Gluttonous Grimoire, Soul Gem, Erosion, Eye of Providence, Hydra''s Lament,
    Oni Hunter''s Garb, Shield of the Phoenix, The Reaper, Stone of Binding, Helm
    of Darkness, Helm of Radiance, Midgardian Mail, Magi''s Cloak, Titan''s Bane,
    Avenging Blade, Mantle Of Discord, Leviathan''s Hide, Screeching Gargoyle, Spear
    of Desolation, Wyrmskin Hide, Obsidian Shard, Arondight, Ancile, Blood-Bound Book,
    Hide of the Nemean Lion, Sanguine Lash, Death Metal, Stampede, Void Stone, Void
    Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.62
    Shield Splitter:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.59
      efficiency: 0.58
      win: 0.69
      pick: 0.22
      fit: 0.47
    Shifter's Shield:
      total: 0.58
      efficiency: 0.47
      win: 0.74
      pick: 0.16
      fit: 0.52
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.71
      pick: 0.18
      fit: 0.52
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Soul Gem, Shield of the Phoenix, The Reaper,
    Jotunn''s Revenge, Berserker''s Shield, Shield Splitter, Gluttonous Grimoire,
    Blood-Bound Book, Phoenix Feather, Yogi''s Necklace, Bloodforge, Ethereal Staff,
    Hydra''s Lament, Oni Hunter''s Garb, Erosion, Chandra''s Grace, Eye of Providence,
    Avenging Blade, Bancroft''s Talon, Midgardian Mail, Regrowth Striders, Titan''s
    Bane, Rod of Asclepius, Leviathan''s Hide, Helm of Radiance, Glorious Pridwen,
    Wyrmskin Hide, Sphere of Negation, Stone of Binding, Spear of Desolation, Helm
    of Darkness, Soul Locket, Arondight.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.6
    Shifter's Shield:
      total: 0.58
      efficiency: 0.47
      win: 0.74
      pick: 0.16
      fit: 0.5
    Freya's Tears:
      total: 0.59
      efficiency: 0.58
      win: 0.69
      pick: 0.22
      fit: 0.41
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.65
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Stone of Binding
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Gluttonous Grimoire, Amanita Charm,
    Soul Gem, Stone of Binding, Screeching Gargoyle, Avenging Blade, The Reaper, Berserker''s
    Shield, Shield Splitter, Titan''s Bane, Obsidian Shard, Spear of Desolation, Void
    Stone, Void Shield, The Crusher, Spear of the Magus, Heartseeker, Hydra''s Lament,
    Oni Hunter''s Garb, Erosion, Eye of Providence, Helm of Radiance, Doom Orb, Tekko-Kagi,
    Shield of the Phoenix, The World Stone, Midgardian Mail, Helm of Darkness, Magi''s
    Cloak, Leviathan''s Hide, Mantle Of Discord, Dreamer''s Idol, Blood-Bound Book.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.5
      win: 0.65
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.49
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.69
      pick: 0.22
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.65
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
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
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Nimble Ring, Jotunn''s
    Revenge, Golden Blade, Shield Splitter, Gluttonous Grimoire, Tyrfing, Soul Gem,
    Tekko-Kagi, Pharaoh''s Curse, Lernaean Bow, Toxic Blade, Oni Hunter''s Garb, Hydra''s
    Lament, Shogun''s Ofuda, Silverbranch Bow, Eros'' Bow, Helm of Radiance, Erosion,
    Eye of Providence, Stone of Binding, Midgardian Mail, Obsidian Shard, Shield of
    the Phoenix, Spear of Desolation, The Reaper, Helm of Darkness, Magi''s Cloak,
    Screeching Gargoyle, Titan''s Bane, Riptalon, Leviathan''s Hide, Dominance, Mantle
    Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.65
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.62
      efficiency: 0.74
      win: 0.65
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.47
    Nimble Ring:
      total: 0.56
      efficiency: 0.63
      win: 0.65
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.69
      pick: 0.22
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Soul Gem, Amanita Charm, Berserker''s Shield, Spear of Desolation, Gluttonous
    Grimoire, Hydra''s Lament, Shield of the Phoenix, Shield Splitter, Screeching
    Gargoyle, Lotus Sickle, Chronos'' Pendant, Arondight, Helm of Radiance, Prophetic
    Cloak, Oni Hunter''s Garb, Erosion, Helm of Darkness, Eye of Providence, Obsidian
    Shard, Stone of Binding, Gladiator''s Shield, Gem of Focus, Midgardian Mail, Blood-Bound
    Book, Magi''s Cloak, Heartwood Charm, Mantle Of Discord, Leviathan''s Hide, The
    Reaper, Ancient Signet, Regrowth Striders, Chandra''s Grace, Eye of Erebus.'
  slot_scores:
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.63
      win: 0.67
      pick: 0.2
      fit: 0.44
    Genji's Guard:
      total: 0.59
      efficiency: 0.69
      win: 0.61
      pick: 0.23
      fit: 0.44
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.51
    Freya's Tears:
      total: 0.61
      efficiency: 0.58
      win: 0.69
      pick: 0.22
      fit: 0.59
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.65
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Gluttonous Grimoire, Soul Gem, The Reaper,
    Tekko-Kagi, Titan''s Bane, Hydra''s Lament, Golden Blade, Nimble Ring, Obsidian
    Shard, Spear of Desolation, Tyrfing, The Crusher, Oni Hunter''s Garb, Lernaean
    Bow, Erosion, Avenging Blade, Eye of Providence, Helm of Radiance, Heartseeker,
    Stone of Binding, Shield of the Phoenix, Midgardian Mail, Arondight, Helm of Darkness,
    Magi''s Cloak, Spear of the Magus, Screeching Gargoyle, Death Metal, Pharaoh''s
    Curse, Toxic Blade, Leviathan''s Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.74
      win: 0.65
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.49
    Shield Splitter:
      total: 0.57
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.69
      pick: 0.22
      fit: 0.35
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Shield Splitter
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    Jotunn''s Revenge, Amanita Charm, Soul Gem, Shield Splitter, Berserker''s Shield,
    Obsidian Shard, Spear of Desolation, Helm of Radiance, The Reaper, Titan''s Bane,
    Helm of Darkness, Spear of the Magus, Hydra''s Lament, Blood-Bound Book, Death
    Metal, Oni Hunter''s Garb, Ancient Signet, Erosion, Lotus Sickle, Eye of Providence,
    The Crusher, Jade Scepter, Doom Orb, Stone of Binding, Shield of the Phoenix,
    Midgardian Mail, Avenging Blade, The World Stone, Magi''s Cloak, Chronos'' Pendant,
    Heartseeker, Screeching Gargoyle, Leviathan''s Hide, Mantle Of Discord.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.63
      win: 0.67
      pick: 0.2
      fit: 0.21
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.49
    Shield Splitter:
      total: 0.57
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.69
      pick: 0.22
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Genji's Guard
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
    Revenge, Berserker''s Shield, Gluttonous Grimoire, Soul Gem, Erosion, Eye of Providence,
    Hydra''s Lament, Oni Hunter''s Garb, Shield of the Phoenix, The Reaper, Stone
    of Binding, Helm of Darkness, Helm of Radiance, Midgardian Mail, Magi''s Cloak,
    Titan''s Bane, Avenging Blade, Mantle Of Discord, Leviathan''s Hide, Screeching
    Gargoyle, Spear of Desolation, Wyrmskin Hide, Obsidian Shard, Arondight, Ancile,
    Blood-Bound Book, Hide of the Nemean Lion, Sanguine Lash, Death Metal, Stampede,
    Void Stone, Void Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.33
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.61
      pick: 0.23
      fit: 0.28
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.65
      pick: 0.15
      fit: 0.62
    Shield Splitter:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
---
