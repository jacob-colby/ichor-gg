---
type: smite-build
god: Cupid
mode: Conquest
builds:
- source: community
  aspect: Aspect of Love
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.36
  slot_order:
  - name: Tyrfing
    pick_rate: 0.55
    win_rate: 0.6
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.14
      win_rate: 0.64
    - name: Dominance
      pick_rate: 0.06
      win_rate: 0.52
  - name: Odysseus' Bow
    pick_rate: 0.33
    win_rate: 0.61
    alternates:
    - name: Dagger of Frenzy
      pick_rate: 0.09
      win_rate: 0.62
    - name: Toxic Blade
      pick_rate: 0.09
      win_rate: 0.65
  - name: Silverbranch Bow
    pick_rate: 0.14
    win_rate: 0.69
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.15
      win_rate: 0.61
    - name: The Executioner
      pick_rate: 0.14
      win_rate: 0.65
  - name: The Executioner
    pick_rate: 0.19
    win_rate: 0.64
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.26
      win_rate: 0.6
    - name: Riptalon
      pick_rate: 0.11
      win_rate: 0.63
  - name: Riptalon
    pick_rate: 0.14
    win_rate: 0.69
    alternates:
    - name: The Executioner
      pick_rate: 0.13
      win_rate: 0.65
    - name: Silverbranch Bow
      pick_rate: 0.12
      win_rate: 0.54
  - name: Hunter's Bow
    pick_rate: 0.12
    win_rate: 0.46
    alternates:
    - name: Manchu Bow
      pick_rate: 0.12
      win_rate: 0.59
    - name: Riptalon
      pick_rate: 0.08
      win_rate: 0.65
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.31
    win_rate: 0.66
  - name: Death's Embrace
    pick_rate: 0.16
    win_rate: 0.63
  - name: Leather Cowl
    pick_rate: 0.16
    win_rate: 0.51
  source_url: https://smitebrain.com/gods/cupid/
  last_verified: '2026-08-21'
  god_win_rate: 0.5963777490297542
  god_matches_won: 461
  god_matches_played: 773
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Soul Gem, Death Metal,
    Gluttonous Grimoire, Berserker''s Shield, Spear of Desolation, The Crusher, Spear
    of the Magus, Obsidian Shard, Genji''s Guard, Breastplate of Valor, Lernaean Bow,
    The Reaper, Toxic Blade, Hydra''s Lament, Golden Blade, Bragi''s Harp, Tekko-Kagi,
    Heartseeker, Runeforged Hammer, Freya''s Tears, Bracer of The Abyss, Amanita Charm,
    Helm of Radiance, Chronos'' Pendant, Kinetic Cuirass, Doom Orb, The Cosmic Horror,
    Deathbringer, Damaru, Ancient Signet, The World Stone, Ethereal Staff, Pharaoh''s
    Curse, Rod of Asclepius, Blood-Bound Book, Titan''s Bane.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.44
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.69
      pick: 0.3
      fit: 0.46
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.69
      pick: 0.22
      fit: 0.39
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.62
      pick: 0.0
      fit: 0.27
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Silverbranch Bow
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire,
    Berserker''s Shield, The Crusher, Spear of Desolation, Spear of the Magus, Hydra''s
    Lament, Genji''s Guard, Breastplate of Valor, Obsidian Shard, Lernaean Bow, Bragi''s
    Harp, Heartseeker, The Reaper, Golden Blade, Runeforged Hammer, Ancient Signet,
    Tekko-Kagi, Doom Orb, Helm of Radiance, The World Stone, Bracer of The Abyss,
    Amanita Charm, Chronos'' Pendant, Freya''s Tears, Kinetic Cuirass, The Cosmic
    Horror, Ethereal Staff, Deathbringer, Damaru, Rod of Asclepius, Bancroft''s Talon,
    Wish-Granting Pearl, Blood-Bound Book, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.41
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.41
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.48
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.69
      pick: 0.3
      fit: 0.38
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.69
      pick: 0.22
      fit: 0.32
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.62
      pick: 0.0
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Damaru
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Damaru
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Gluttonous Grimoire, Berserker''s Shield, Spear of Desolation, The Crusher, Spear
    of the Magus, Obsidian Shard, Genji''s Guard, Breastplate of Valor, The Reaper,
    Lernaean Bow, Hydra''s Lament, Toxic Blade, Golden Blade, Bragi''s Harp, Tekko-Kagi,
    Freya''s Tears, Heartseeker, Runeforged Hammer, Amanita Charm, Helm of Radiance,
    Bracer of The Abyss, Chronos'' Pendant, Kinetic Cuirass, Deathbringer, Damaru,
    Doom Orb, The Cosmic Horror, Ancient Signet, The World Stone, Ethereal Staff,
    Rod of Asclepius, Blood-Bound Book, Pharaoh''s Curse, Dreamer''s Idol.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.35
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.46
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.69
      pick: 0.3
      fit: 0.44
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.69
      pick: 0.22
      fit: 0.37
    Damaru:
      total: 0.5
      efficiency: 0.5
      win: 0.62
      pick: 0.0
      fit: 0.32
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - Riptalon
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Jotunn''s Revenge, Soul Gem, Gluttonous Grimoire, Nimble Ring,
    Death Metal, Spear of Desolation, Berserker''s Shield, The Crusher, Spear of the
    Magus, Obsidian Shard, Genji''s Guard, The Reaper, Breastplate of Valor, Hydra''s
    Lament, Toxic Blade, Tekko-Kagi, Heartseeker, Lernaean Bow, Golden Blade, Freya''s
    Tears, Bragi''s Harp, Runeforged Hammer, Doom Orb, The Cosmic Horror, Amanita
    Charm, Chronos'' Pendant, The World Stone, Helm of Radiance, Titan''s Bane, Kinetic
    Cuirass, Bracer of The Abyss, Dreamer''s Idol, Ancient Signet, Deathbringer, Damaru,
    Ethereal Staff, Shield of the Phoenix, Rod of Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.43
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.69
      pick: 0.3
      fit: 0.47
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.69
      pick: 0.22
      fit: 0.41
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.62
      pick: 0.0
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Riptalon
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Silverbranch Bow
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Soul Gem, Jotunn''s Revenge, Berserker''s
    Shield, Shield of the Phoenix, Gluttonous Grimoire, Ethereal Staff, Rod of Asclepius,
    The Reaper, Nimble Ring, Kinetic Cuirass, Death Metal, Blood-Bound Book, Genji''s
    Guard, Breastplate of Valor, Freya''s Tears, Bancroft''s Talon, Chandra''s Grace,
    The Crusher, Spear of Desolation, Yogi''s Necklace, Runeforged Hammer, Pharaoh''s
    Curse, Spear of the Magus, Golden Blade, Phoenix Feather, Lifebinder, Helm of
    Radiance, Obsidian Shard, Shogun''s Ofuda, Shifter''s Shield, Sphere of Negation,
    Mantle Of Discord, Shield Splitter, Hydra''s Lament, Stone of Binding, Lernaean
    Bow, Spectral Armor.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.62
      pick: 0.0
      fit: 0.37
    Riptalon:
      total: 0.6
      efficiency: 0.51
      win: 0.69
      pick: 0.3
      fit: 0.63
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.69
      pick: 0.22
      fit: 0.28
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Riptalon
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Soul Gem, Gluttonous Grimoire,
    Nimble Ring, Death Metal, Spear of Desolation, The Crusher, Spear of the Magus,
    Berserker''s Shield, Obsidian Shard, The Reaper, Screeching Gargoyle, Toxic Blade,
    Stone of Binding, Avenging Blade, Tekko-Kagi, Heartseeker, Genji''s Guard, Breastplate
    of Valor, Doom Orb, The Cosmic Horror, The World Stone, Lernaean Bow, Hydra''s
    Lament, Titan''s Bane, Dreamer''s Idol, Golden Blade, Amanita Charm, Freya''s
    Tears, Runeforged Hammer, Bragi''s Harp, Kinetic Cuirass, Helm of Radiance, Void
    Shield, Bracer of The Abyss, Chronos'' Pendant, Void Stone, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.12
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.1
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.69
      pick: 0.3
      fit: 0.53
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.69
      pick: 0.22
      fit: 0.47
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.62
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Soul Gem, Death Metal,
    Gluttonous Grimoire, Berserker''s Shield, Spear of Desolation, The Crusher, Spear
    of the Magus, Toxic Blade, Golden Blade, Genji''s Guard, Breastplate of Valor,
    Obsidian Shard, Lernaean Bow, The Reaper, Hydra''s Lament, Bragi''s Harp, Tekko-Kagi,
    Bracer of The Abyss, Freya''s Tears, Amanita Charm, Runeforged Hammer, Heartseeker,
    Helm of Radiance, Kinetic Cuirass, Chronos'' Pendant, Pharaoh''s Curse, Doom Orb,
    The Cosmic Horror, Ancient Signet, Ethereal Staff, The World Stone, Deathbringer,
    Damaru, Rod of Asclepius, Blood-Bound Book, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.32
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.38
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.4
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.69
      pick: 0.3
      fit: 0.51
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.69
      pick: 0.22
      fit: 0.44
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.62
      pick: 0.0
      fit: 0.25
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Spear of Desolation
  - Silverbranch Bow
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Soul Gem, Nimble Ring, Spear of Desolation, Genji''s Guard, Breastplate of Valor,
    Gluttonous Grimoire, Berserker''s Shield, Death Metal, Hydra''s Lament, Freya''s
    Tears, The Crusher, Chronos'' Pendant, Spear of the Magus, Shield of the Phoenix,
    Obsidian Shard, Toxic Blade, Lernaean Bow, Screeching Gargoyle, The Reaper, Amanita
    Charm, Golden Blade, Arondight, Tekko-Kagi, Kinetic Cuirass, Gem of Focus, Runeforged
    Hammer, Heartseeker, Helm of Radiance, Bracer of The Abyss, Bragi''s Harp, Totem
    of Death, Pharaoh''s Curse, Pendulum Blade, Eye of Providence, Doom Orb, The Cosmic
    Horror, Deathbringer.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.46
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.46
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.69
      pick: 0.22
      fit: 0.35
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.62
      pick: 0.0
      fit: 0.2
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Soul Gem,
    Death Metal, Gluttonous Grimoire, Berserker''s Shield, Spear of Desolation, The
    Crusher, Spear of the Magus, Obsidian Shard, Genji''s Guard, Breastplate of Valor,
    Lernaean Bow, The Reaper, Hydra''s Lament, Golden Blade, Bragi''s Harp, Tekko-Kagi,
    Heartseeker, Runeforged Hammer, Freya''s Tears, Bracer of The Abyss, Amanita Charm,
    Helm of Radiance, Chronos'' Pendant, Kinetic Cuirass, Doom Orb, The Cosmic Horror,
    Deathbringer, Damaru, Ancient Signet, The World Stone, Ethereal Staff, Pharaoh''s
    Curse, Toxic Blade, Rod of Asclepius, Blood-Bound Book, Titan''s Bane.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.62
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.62
      pick: 0.0
      fit: 0.27
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - Riptalon
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Riptalon
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Nimble Ring, Soul Gem, Death Metal, Gluttonous Grimoire, Berserker''s Shield,
    Spear of Desolation, The Crusher, Spear of the Magus, Obsidian Shard, Genji''s
    Guard, Breastplate of Valor, Lernaean Bow, The Reaper, Hydra''s Lament, Golden
    Blade, Bragi''s Harp, Tekko-Kagi, Heartseeker, Runeforged Hammer, Freya''s Tears,
    Bracer of The Abyss, Amanita Charm, Helm of Radiance, Chronos'' Pendant, Kinetic
    Cuirass, Doom Orb, The Cosmic Horror, Deathbringer, Damaru, Ancient Signet, The
    World Stone, Ethereal Staff, Pharaoh''s Curse, Toxic Blade, Rod of Asclepius,
    Blood-Bound Book, Titan''s Bane.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.39
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.37
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.69
      pick: 0.3
      fit: 0.46
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.69
      pick: 0.22
      fit: 0.39
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.62
      pick: 0.0
      fit: 0.27
  swaps:
  - added: Riptalon
    removed: Berserker's Shield
    reason: community 69% win over 108 matches (vs 60% on this god), taking the model's
      weakest slot from Berserker's Shield
  - added: Silverbranch Bow
    removed: Death Metal
    reason: community 69% win over 108 matches (vs 60% on this god), taking the model's
      weakest slot from Death Metal
  starter: *id001
---
