---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.42
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.51
    win_rate: 0.69
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.22
      win_rate: 0.32
    - name: Transcendence
      pick_rate: 0.07
      win_rate: 0.29
  - name: Sanguine Lash
    pick_rate: 0.22
    win_rate: 0.77
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.5
    - name: Jotunn's Revenge
      pick_rate: 0.08
      win_rate: 0.38
  - name: Freya's Tears
    pick_rate: 0.22
    win_rate: 0.64
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.12
      win_rate: 0.33
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.44
  - name: Umbral Link
    pick_rate: 0.11
    win_rate: 0.55
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.53
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.33
  - name: The Reaper
    pick_rate: 0.08
    win_rate: 0.86
    alternates:
    - name: Gluttonous Grimoire
      pick_rate: 0.07
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.67
  - name: Evil Eye
    pick_rate: 0.05
    win_rate: 0.0
    alternates:
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.5
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.42
    win_rate: 0.64
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.4
  - name: Hunter's Cowl
    pick_rate: 0.15
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-11-06'
  god_win_rate: 0.5445544554455446
  god_matches_won: 55
  god_matches_played: 101
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - The Reaper
  flex_slots:
  - Shield Splitter
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Kinetic Cuirass,
    Shield Splitter, Golden Blade, Runeforged Hammer, Tyrfing, Soul Gem, Oni Hunter''s
    Garb, Hydra''s Lament, Shield of the Phoenix, Draconic Scale, Breastplate of Valor,
    Avenging Blade, Genji''s Guard, Death Metal, Bragi''s Harp, Nimble Ring, Blood-Bound
    Book, Erosion, Eye of Providence, Midgardian Mail, The Crusher, Spear of Desolation,
    Leviathan''s Hide, Wyrmskin Hide, Lernaean Bow, Dominance, Heartseeker, Hide of
    the Nemean Lion, Tekko-Kagi, Shogun''s Ofuda, Pharaoh''s Curse, Triton''s Conch,
    Helm of Radiance, Jotunn''s Revenge.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.61
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.5
    Shield Splitter:
      total: 0.51
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.64
      pick: 0.34
      fit: 0.26
    The Reaper:
      total: 0.66
      efficiency: 0.57
      win: 0.86
      pick: 0.17
      fit: 0.4
  community_ordered:
  - Freya's Tears
  - The Reaper
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Shield of the Phoenix,
    Rod of Tahuti, Soul Gem, Blood-Bound Book, Shield Splitter, Phoenix Feather, Yogi''s
    Necklace, Runeforged Hammer, Ethereal Staff, Golden Blade, Draconic Scale, Tyrfing,
    Oni Hunter''s Garb, Erosion, Eye of Providence, Bloodforge, Bancroft''s Talon,
    Breastplate of Valor, Chandra''s Grace, Riptalon, Genji''s Guard, Midgardian Mail,
    Hydra''s Lament, Leviathan''s Hide, Hide of the Nemean Lion, Avenging Blade, Regrowth
    Striders, Shogun''s Ofuda, Wyrmskin Hide, Pharaoh''s Curse, Death Metal, Nimble
    Ring, Stone of Binding, Jotunn''s Revenge.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.59
    Shield Splitter:
      total: 0.51
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.5
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.34
      fit: 0.33
    The Reaper:
      total: 0.69
      efficiency: 0.57
      win: 0.86
      pick: 0.17
      fit: 0.64
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Freya's Tears
  - The Reaper
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - The Reaper
  - Spear of Desolation
  flex_slots:
  - Avenging Blade
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Berserker''s Shield, Soul Gem, Amanita Charm, Kinetic
    Cuirass, Avenging Blade, Spear of Desolation, The Crusher, Heartseeker, Screeching
    Gargoyle, Stone of Binding, Tekko-Kagi, Titan''s Bane, Obsidian Shard, Void Stone,
    Void Shield, Shield Splitter, Runeforged Hammer, Toxic Blade, Tyrfing, Spear of
    the Magus, Jotunn''s Revenge, Golden Blade, Dreamer''s Idol, Silverbranch Bow,
    Breastplate of Valor, Oni Hunter''s Garb, Riptalon, Hydra''s Lament, Shield of
    the Phoenix, Genji''s Guard, Avatar''s Parashu, Doom Orb, Blood-Bound Book, Draconic
    Scale, Death Metal, Nimble Ring, The World Stone.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.7
    Berserker's Shield:
      total: 0.53
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.29
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.64
      pick: 0.34
      fit: 0.19
    The Reaper:
      total: 0.68
      efficiency: 0.57
      win: 0.86
      pick: 0.17
      fit: 0.57
    Spear of Desolation:
      total: 0.51
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Freya's Tears
  - The Reaper
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Tyrfing
  - Freya's Tears
  - Sanguine Lash
  - The Reaper
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Tyrfing, Golden Blade,
    Kinetic Cuirass, Nimble Ring, Soul Gem, Toxic Blade, Shield Splitter, Runeforged
    Hammer, Bragi''s Harp, Breastplate of Valor, Oni Hunter''s Garb, Shogun''s Ofuda,
    Pharaoh''s Curse, Lernaean Bow, Dominance, Silverbranch Bow, Shield of the Phoenix,
    Genji''s Guard, Riptalon, Tekko-Kagi, Blood-Bound Book, Hydra''s Lament, Draconic
    Scale, Qin''s Blade, Spear of Desolation, Midgardian Mail, Bracer of The Abyss,
    Erosion, Death Metal, Ancient Signet, Leviathan''s Hide, Eye of Providence, Helm
    of Radiance, Hide of the Nemean Lion, Jotunn''s Revenge.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.64
      pick: 0.34
      fit: 0.19
    Sanguine Lash:
      total: 0.56
      efficiency: 0.4
      win: 0.77
      pick: 0.3
      fit: 0.39
    The Reaper:
      total: 0.63
      efficiency: 0.57
      win: 0.86
      pick: 0.17
      fit: 0.25
  community_ordered:
  - Freya's Tears
  - Sanguine Lash
  - The Reaper
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Berserker''s
    Shield, Breastplate of Valor, Amanita Charm, Spear of Desolation, Shield of the
    Phoenix, Genji''s Guard, Kinetic Cuirass, Hydra''s Lament, Screeching Gargoyle,
    Chronos'' Pendant, Arondight, Gladiator''s Shield, Shield Splitter, Blood-Bound
    Book, Runeforged Hammer, Gem of Focus, Heartwood Charm, Tyrfing, Oni Hunter''s
    Garb, Chandra''s Grace, Jotunn''s Revenge, Nimble Ring, Golden Blade, Eye of Erebus,
    Ancient Signet, Helm of Radiance, Draconic Scale, Prophetic Cloak, Damaru, Death
    Metal, Midgardian Mail, Polynomicon, Regrowth Striders, Erosion, Obsidian Shard,
    Jade Scepter.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.29
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.34
      fit: 0.48
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.82
      win: 0.53
      pick: 0.0
      fit: 0.13
    Soul Gem:
      total: 0.54
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.64
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
  - Genji's Guard
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Jotunn''s Revenge, Genji''s Guard, Shield Splitter, Golden Blade, Runeforged
    Hammer, Tyrfing, Soul Gem, Oni Hunter''s Garb, Hydra''s Lament, Shield of the
    Phoenix, Draconic Scale, Breastplate of Valor, Avenging Blade, Death Metal, Bragi''s
    Harp, Nimble Ring, Blood-Bound Book, Erosion, Eye of Providence, Midgardian Mail,
    The Crusher, Spear of Desolation, Leviathan''s Hide, Wyrmskin Hide, Lernaean Bow,
    Dominance, Heartseeker, Hide of the Nemean Lion, Tekko-Kagi, Shogun''s Ofuda,
    Pharaoh''s Curse, Triton''s Conch, Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.71
      win: 0.44
      pick: 0.14
      fit: 0.15
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.65
      win: 0.38
      pick: 0.11
      fit: 0.33
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.5
    Shield Splitter:
      total: 0.51
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Devourer's Gauntlet
  - Kinetic Cuirass
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
  - Devourer's Gauntlet
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Rod of Tahuti,
    Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Genji''s Guard, Shield Splitter,
    Golden Blade, Runeforged Hammer, Tyrfing, Soul Gem, Oni Hunter''s Garb, Hydra''s
    Lament, Shield of the Phoenix, Draconic Scale, Breastplate of Valor, Avenging
    Blade, Death Metal, Bragi''s Harp, Nimble Ring, Blood-Bound Book, Erosion, Eye
    of Providence, Midgardian Mail, The Crusher, Spear of Desolation, Leviathan''s
    Hide, Wyrmskin Hide, Lernaean Bow, Dominance, Heartseeker, Hide of the Nemean
    Lion, Tekko-Kagi, Shogun''s Ofuda, Pharaoh''s Curse, Triton''s Conch, Helm of
    Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.71
      win: 0.44
      pick: 0.14
      fit: 0.15
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.65
      win: 0.38
      pick: 0.11
      fit: 0.33
    Devourer's Gauntlet:
      total: 0.53
      efficiency: 0.4
      win: 0.69
      pick: 0.51
      fit: 0.35
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.82
      win: 0.53
      pick: 0.0
      fit: 0.11
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Devourer's Gauntlet
  swaps:
  - added: Devourer's Gauntlet
    removed: Shield Splitter
    reason: community 69% win over 52 matches (vs 54% on this god), taking the model's
      weakest slot from Shield Splitter
  starter: *id001
---
